"""
SQLite caching engine for Algerian Precipitation Explorer.
Stores retrieved ERA5 and GPCC records by (lat, lon, year) to eliminate redundant API/network calls.
"""

import sqlite3
import json
import os
from typing import Optional, Dict, Any, List

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "precipitation_cache.db")

def get_db_connection() -> sqlite3.Connection:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS annual_cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grid_lat REAL NOT NULL,
            grid_lon REAL NOT NULL,
            year INTEGER NOT NULL,
            source_dataset TEXT NOT NULL,
            spatial_resolution TEXT NOT NULL,
            annual_sum_mm REAL NOT NULL,
            monthly_data_json TEXT NOT NULL,
            daily_data_json TEXT,
            hourly_data_json TEXT,
            data_quality_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(grid_lat, grid_lon, year)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS location_normals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grid_lat REAL NOT NULL,
            grid_lon REAL NOT NULL,
            period_label TEXT NOT NULL,
            mean_annual_mm REAL NOT NULL,
            monthly_normals_json TEXT NOT NULL,
            wettest_year INTEGER,
            wettest_val REAL,
            driest_year INTEGER,
            driest_val REAL,
            trend_slope_decade REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(grid_lat, grid_lon, period_label)
        )
    """)
    conn.commit()
    conn.close()

def get_cached_year(lat: float, lon: float, year: int) -> Optional[Dict[str, Any]]:
    # Round coordinates to ~0.05 deg precision for cache matching
    rlat = round(lat, 2)
    rlon = round(lon, 2)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM annual_cache 
        WHERE ABS(grid_lat - ?) < 0.05 AND ABS(grid_lon - ?) < 0.05 AND year = ?
        LIMIT 1
    """, (rlat, rlon, year))
    row = cursor.fetchone()
    conn.close()
    if row:
        year_val = row["year"]
        is_gpcc = year_val < 1940
        return {
            "grid_lat": row["grid_lat"],
            "grid_lon": row["grid_lon"],
            "year": year_val,
            "dataset": row["source_dataset"],
            "source_dataset": row["source_dataset"],
            "spatial_resolution": row["spatial_resolution"],
            "annual_sum_mm": row["annual_sum_mm"],
            "monthly_data": json.loads(row["monthly_data_json"]),
            "daily_data": json.loads(row["daily_data_json"]) if row["daily_data_json"] else None,
            "hourly_data": json.loads(row["hourly_data_json"]) if row["hourly_data_json"] else None,
            "data_quality": json.loads(row["data_quality_json"]) if row["data_quality_json"] else None,
            "temporal_resolution": "Données mensuelles agrégées" if is_gpcc else "Cumuls journaliers et pas horaires",
            "observation_type": "Analyse pluviométrique sur grille (WMO / GPCC v2022)" if is_gpcc else "Réanalyse atmosphérique (ECMWF ERA5 / Assimilation 4D-Var)",
            "daily_hourly_available": not is_gpcc
        }
    return None

def save_cached_year(lat: float, lon: float, year: int, source_dataset: str,
                     spatial_resolution: str, annual_sum_mm: float,
                     monthly_data: list, daily_data: Optional[list] = None,
                     hourly_data: Optional[list] = None,
                     data_quality: Optional[dict] = None):
    rlat = round(lat, 2)
    rlon = round(lon, 2)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO annual_cache 
        (grid_lat, grid_lon, year, source_dataset, spatial_resolution, 
         annual_sum_mm, monthly_data_json, daily_data_json, hourly_data_json, data_quality_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        rlat, rlon, year, source_dataset, spatial_resolution,
        annual_sum_mm,
        json.dumps(monthly_data),
        json.dumps(daily_data) if daily_data else None,
        json.dumps(hourly_data) if hourly_data else None,
        json.dumps(data_quality) if data_quality else None
    ))
    conn.commit()
    conn.close()
