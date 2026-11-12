"""
FastAPI Server for Algeria Hydro-Replay: Historical Precipitation Explorer.
Inspired by Copernicus Climate Change Service & Weather Replay.
"""

from fastapi import FastAPI, Query, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
import io
import csv

from backend.algeria_geo import WILAYAS, search_locations, find_nearest_wilaya
from backend.database import init_db
from backend.data_engine import (
    get_precipitation_year,
    get_annual_timeline,
    get_algeria_map_distribution,
    compare_locations_or_years
)
from backend.era5_provider import fetch_era5_hourly

# Initialize SQLite database
init_db()

app = FastAPI(
    title="Algeria Hydro-Replay (Météo Replay Algérie)",
    description="Scientific Historical Precipitation Data Explorer for Algeria (1900-Present), powered by GPCC and Copernicus ERA5.",
    version="1.0.0"
)

# Enable CORS for scientific web integrations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static")
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static folder
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def get_index():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Algeria Hydro-Replay API Active. Static frontend loading..."}

@app.get("/api/wilayas")
def list_wilayas():
    """List all 58 Wilayas of Algeria with geographical coordinates and bioclimatic zones."""
    return {"wilayas": WILAYAS, "count": len(WILAYAS)}

@app.get("/api/locations/search")
def location_search(q: str = Query(..., min_length=1, description="Wilaya or commune name")):
    """Autocomplete search for Algerian Wilayas and Communes."""
    return {"results": search_locations(q)}

@app.get("/api/precipitation")
def get_precipitation(
    lat: float = Query(..., ge=18.0, le=39.0, description="Latitude in Algeria (18°N to 39°N)"),
    lon: float = Query(..., ge=-9.0, le=13.0, description="Longitude in Algeria (-9°W to 13°E)"),
    year: int = Query(..., ge=1900, le=2026, description="Year between 1900 and present")
):
    """
    Retrieve historical precipitation for a specific coordinate and year.
    Uses GPCC (1900-1939) or Copernicus ERA5 (1940-present).
    """
    try:
        data = get_precipitation_year(lat=lat, lon=lon, year=year)
        nearest = find_nearest_wilaya(lat, lon)
        data["nearest_wilaya"] = nearest.get("wilaya", {}).get("name")
        data["nearest_wilaya_ar"] = nearest.get("wilaya", {}).get("name_ar")
        data["wilaya_code"] = nearest.get("wilaya", {}).get("code")
        data["distance_to_wilaya_center_km"] = nearest.get("distance_km")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Data retrieval failed: {str(e)}")

@app.get("/api/precipitation/timeline")
def get_timeline(
    lat: float = Query(..., ge=18.0, le=39.0),
    lon: float = Query(..., ge=-9.0, le=13.0),
    start_year: int = Query(1900, ge=1900),
    end_year: int = Query(2025, le=2026)
):
    """
    Generate 1900-present annual timeline, decadal averages, trends and climatological normals.
    """
    try:
        return get_annual_timeline(lat=lat, lon=lon, start_year=start_year, end_year=end_year)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Timeline generation failed: {str(e)}")

@app.get("/api/precipitation/hourly")
def get_hourly_precip(
    lat: float = Query(..., ge=18.0, le=39.0),
    lon: float = Query(..., ge=-9.0, le=13.0),
    date: str = Query(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="Date YYYY-MM-DD (1940-present)")
):
    """
    Hourly precipitation reanalysis from ERA5 for extreme events.
    """
    year = int(date.split("-")[0])
    if year < 1940:
        raise HTTPException(
            status_code=400,
            detail="Hourly precipitation data is only available from 1940 onwards via ERA5 Reanalysis. Prior to 1940, meteorological records are preserved at monthly resolution (GPCC)."
        )
    try:
        return fetch_era5_hourly(lat=lat, lon=lon, date_str=date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hourly data retrieval failed: {str(e)}")

@app.get("/api/map/distribution")
def get_map_distribution(year: int = Query(..., ge=1900, le=2026)):
    """
    Choropleth and point distribution across all 58 Wilayas of Algeria for the selected year.
    """
    try:
        return get_algeria_map_distribution(year=year)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Map distribution failed: {str(e)}")

class CompareRequest(BaseModel):
    locations: List[Dict[str, Any]]
    years: List[int]

@app.post("/api/compare")
def compare_records(req: CompareRequest):
    """
    Multi-year and multi-location historical precipitation comparison.
    """
    try:
        if not req.locations or not req.years:
            raise HTTPException(status_code=400, detail="Locations and years must not be empty.")
        return compare_locations_or_years(locations=req.locations, years=req.years)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Comparison failed: {str(e)}")

@app.get("/api/export/csv")
def export_csv(
    lat: float = Query(...),
    lon: float = Query(...),
    start_year: int = Query(1900, ge=1900),
    end_year: int = Query(2025, le=2026),
    location_name: Optional[str] = Query("Algeria_Location")
):
    """
    Export historical precipitation records as scientific CSV for hydrological studies.
    """
    timeline = get_annual_timeline(lat=lat, lon=lon, start_year=start_year, end_year=end_year)
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Scientific metadata header
    writer.writerow(["# Algeria Hydro-Replay: Historical Precipitation Data Export"])
    writer.writerow(["# Location Name", location_name])
    writer.writerow(["# Latitude", f"{lat:.4f} N"])
    writer.writerow(["# Longitude", f"{lon:.4f} E"])
    writer.writerow(["# Primary Data Sources", "GPCC Full Data Monthly v2022 (1900-1939) | Copernicus ERA5 / ERA5-Land (1940-Present)"])
    writer.writerow(["# Precipitation Units", "Millimeters (mm)"])
    writer.writerow(["# Climatological Normal 1961-1990 (mm)", timeline["statistics"]["normal_1961_1990_mm"]])
    writer.writerow(["# Climatological Normal 1991-2020 (mm)", timeline["statistics"]["normal_1991_2020_mm"]])
    writer.writerow(["# Sen's Trend Slope (mm/decade)", timeline["statistics"]["trend_per_decade_mm"]])
    writer.writerow([])
    writer.writerow(["Year", "Annual_Precipitation_mm", "10yr_Moving_Average_mm", "Data_Source"])
    
    for yr, val, roll in zip(timeline["years"], timeline["annual_precipitation_mm"], timeline["rolling_10yr_mean_mm"]):
        src = "GPCC_v2022_Gridded" if yr < 1940 else "ERA5_Copernicus_Reanalysis"
        writer.writerow([yr, val, roll, src])
        
    output.seek(0)
    filename = f"precipitation_{location_name.replace(' ', '_')}_{start_year}_{end_year}.csv"
    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )
