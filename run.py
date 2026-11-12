"""
Algeria Hydro-Replay Server Launcher.
Run with: python run.py
"""

import uvicorn
import os
import sys

# Ensure project root is in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

if __name__ == "__main__":
    print("=" * 70)
    print("  ALGERIA HYDRO-REPLAY : Météo Replay Algérie")
    print("  Explorateur Historique des Précipitations (1900 - Présent)")
    print("  Data Sources: GPCC (DWD/WMO) & Copernicus ERA5 / ERA5-Land (ECMWF)")
    print("=" * 70)
    print("  Starting server at http://127.0.0.1:8000 ...")
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, reload=True)
