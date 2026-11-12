# Algeria Hydro-Replay : Explorateur Historique des Précipitations (1900 - Présent)
### Inspired by Copernicus Weather Replay & European Centre for Medium-Range Weather Forecasts (ECMWF)

**Algeria Hydro-Replay** is a professional, scientific-grade historical precipitation data explorer designed for hydrological, meteorological, and civil engineering studies across the entire territory of Algeria (1900 to present).

---

## 🌟 Key Features

1. **Full Territorial Geographic Selection**:
   - Comprehensive coverage of **all 58 Algerian Wilayas** (with official numbering 01 to 58, Arabic and French nomenclature).
   - Hundreds of communes and cities dynamically searchable with instant autocomplete.
   - Interactive map point selection and manual GPS coordinate inputs (Latitude N / Longitude E).
   - Automatic grid-cell spatial mapping with distance indicators.

2. **Historical Timeline & Replay (1900 - Present)**:
   - Annual precipitation totals in millimeters (mm).
   - Monthly precipitation breakdown with 12-month hyetographs.
   - Daily precipitation records (available from 1940+ via ERA5).
   - Hourly storm deluge reconstruction (e.g. Inondations de Bab El Oued Novembre 2001, Ghardaïa 2008).
   - Interactive Replay playback slider animating historical rainfall year by year.

3. **Authoritative Scientific Data Sources**:
   - **GPCC (Global Precipitation Climatology Centre - DWD / WMO)**:
     - Gridded rain-gauge monthly analysis (0.5° resolution) covering 1900 to 1939.
     - Preserves original spatial resolution and station network uncertainty metrics.
   - **Copernicus ERA5 & ERA5-Land Reanalysis (ECMWF)**:
     - High-resolution atmospheric reanalysis (0.1° / ~9 km and 0.25° / ~31 km) from 1940 to present.
     - Hourly and daily physical precipitation assimilation.
   - Transparent provenance banners clearly distinguishing between in-situ station observations, gridded analyses, and atmospheric reanalyses.

4. **Climatological & Statistical Analysis**:
   - WMO 30-year Climatological Normals comparison: **Normal 1961-1990** vs **Normal 1991-2020**.
   - Long-term secular trends via **Sen's Slope (mm/decade)**.
   - Wettest and driest recorded years in history.
   - 10-year rolling moving average to identify multi-decadal dry and pluvial cycles.

5. **Interactive Algerian Precipitation Distribution Map**:
   - Color-coded intensity zones across all 58 Wilayas:
     - 🔴 **Très faible** (< 100 mm - Saharan)
     - 🟠 **Faible** (100 - 300 mm - Arid)
     - 🟡 **Modéré** (300 - 600 mm - Semi-arid / High Plateaus)
     - 🟢 **Élevé** (600 - 900 mm - Sub-humid)
     - 🔵 **Très élevé** (> 900 mm - Humid coastal mountain ranges)

6. **Historical Comparison Module**:
   - Multi-year comparison for any location (e.g., Algiers in 1900, 1950, 1980, 2000, 2024).
   - Multi-wilaya cross-comparison (e.g., Alger vs Oran vs Constantine vs Ouargla).
   - Preset comparative analyses for historical drought cycles (1921, 1945, 1983, 1994, 2020).

7. **Engineering & Scientific Data Export**:
   - Export structured CSV time-series with full metadata headers for HEC-HMS, ArcGIS, QGIS, or Python hydrological models.
   - Print-ready scientific hydro-meteorological bulletin.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+
- Internet connection (for initial ERA5 live querying; cached queries run offline)

### 2. Launch the Application
Simply run:
```bash
python run.py
```
Or with Uvicorn:
```bash
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 --reload
```

Then open your browser at:
👉 **`http://127.0.0.1:8000`**

---

## 🏛️ Project Architecture

```
WEB HYDRAULIC/
├── backend/
│   ├── app.py               # FastAPI scientific web application & REST endpoints
│   ├── algeria_geo.py       # 58 Algerian Wilayas, communes, bioclimatic classification
│   ├── data_engine.py       # Unified data pipeline, statistical indicators & timeline engine
│   ├── era5_provider.py     # Copernicus ERA5 & ERA5-Land reanalysis client
│   ├── gpcc_provider.py     # GPCC Full Data Monthly v2022 provider
│   └── database.py          # SQLite persistence cache (precipitation_cache.db)
├── static/
│   ├── index.html           # Copernicus Weather Replay dashboard SPA
│   ├── css/
│   │   └── styles.css       # Copernicus C3S design theme, charts & responsive layout
│   └── js/
│       └── app.js           # Client-side map, Chart.js integrations & interactivity
├── data/
│   └── precipitation_cache.db # High-performance SQLite cache
├── requirements.txt         # Dependency specification
├── run.py                   # One-click launcher
└── README.md                # Documentation
```

---

## 📡 REST API Documentation

- `GET /api/wilayas` : List of all 58 Wilayas with coordinates, Arabic names and elevations.
- `GET /api/locations/search?q={query}` : Autocomplete search across Algerian communes and wilayas.
- `GET /api/precipitation?lat={lat}&lon={lon}&year={year}` : Retrieve annual and monthly precipitation, wettest day, and data quality.
- `GET /api/precipitation/timeline?lat={lat}&lon={lon}&start_year=1900&end_year=2025` : Complete 1900-2025 series, 10-year rolling average, normals, and trends.
- `GET /api/precipitation/hourly?lat={lat}&lon={lon}&date={YYYY-MM-DD}` : Hourly precipitation hyetograph (1940+).
- `GET /api/map/distribution?year={year}` : 58 Wilaya choropleth and intensity classification.
- `POST /api/compare` : Multi-year and multi-location side-by-side comparative matrices.
- `GET /api/export/csv?lat={lat}&lon={lon}&start_year=1900&end_year=2025` : Scientific CSV download.
