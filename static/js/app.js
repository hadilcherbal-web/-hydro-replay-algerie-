/**
 * Algeria Hydro-Replay : Explorateur Historique des Précipitations (1900-Présent)
 * Inspired by Copernicus Climate Change Service (C3S) & Weather Replay
 */

// Application State
const state = {
  wilayas: [],
  selectedWilaya: null,
  selectedCommune: null,
  lat: 36.7538,
  lon: 3.0588,
  locationName: "Alger (Alger Centre)",
  currentYear: 1980,
  isPlaying: false,
  playTimer: null,
  activeTab: "tab-dashboard",
  comparisonYears: [1900, 1950, 1980, 2000, 2024],
  comparisonLocations: [
    { name: "Alger", lat: 36.7538, lon: 3.0588 },
    { name: "Oran", lat: 35.698, lon: -0.633 },
    { name: "Constantine", lat: 36.365, lon: 6.614 },
    { name: "Ouargla", lat: 31.953, lon: 5.325 }
  ],
  cachedData: {},
  timelineData: null,
  mapInstance: null,
  mapMarkersLayer: null,
  charts: {
    monthly: null,
    timeline: null,
    compare: null,
    hourly: null
  }
};

// Month Names (French)
const MONTH_NAMES = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"];

document.addEventListener("DOMContentLoaded", () => {
  initUI();
  initMap();
  loadWilayas();
});

// Initialize UI Event Listeners
function initUI() {
  // Welcome Splash Screen
  const splash = document.getElementById("welcome-splash-screen");
  const btnEnter = document.getElementById("btn-enter-platform");
  if (btnEnter && splash) {
    btnEnter.addEventListener("click", () => {
      splash.classList.add("hidden");
    });
  }

  // Global helper to show welcome screen
  window.showWelcomeScreen = function() {
    if (splash) splash.classList.remove("hidden");
  };

  // Tab Switching
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const targetTab = btn.getAttribute("data-tab");
      switchTab(targetTab);
    });
  });

  // Timeline Slider
  const slider = document.getElementById("timeline-slider");
  slider.addEventListener("input", (e) => {
    const yr = parseInt(e.target.value);
    setYear(yr, false);
  });
  slider.addEventListener("change", (e) => {
    const yr = parseInt(e.target.value);
    setYear(yr, true);
  });

  // Replay Animation Play/Pause
  document.getElementById("btn-play-timeline").addEventListener("click", togglePlay);

  // Decade quick buttons
  document.querySelectorAll(".btn-decade").forEach(btn => {
    btn.addEventListener("click", () => {
      const yr = parseInt(btn.getAttribute("data-year"));
      setYear(yr, true);
    });
  });

  // Coordinate manual input
  document.getElementById("btn-apply-coords").addEventListener("click", () => {
    const lat = parseFloat(document.getElementById("input-lat").value);
    const lon = parseFloat(document.getElementById("input-lon").value);
    if (!isNaN(lat) && !isNaN(lon)) {
      setLocation(lat, lon, `Point GPS (${lat.toFixed(3)}N, ${lon.toFixed(3)}E)`);
    }
  });

  // Search input autocomplete
  const searchInput = document.getElementById("input-search");
  let searchTimeout = null;
  searchInput.addEventListener("input", () => {
    clearTimeout(searchTimeout);
    const q = searchInput.value.trim();
    if (q.length < 2) {
      document.getElementById("search-results").style.display = "none";
      return;
    }
    searchTimeout = setTimeout(() => executeSearch(q), 250);
  });

  document.addEventListener("click", (e) => {
    if (!e.target.closest(".search-box-wrapper")) {
      document.getElementById("search-results").style.display = "none";
    }
  });

  // Export CSV
  document.getElementById("btn-export-csv").addEventListener("click", () => {
    const url = `/api/export/csv?lat=${state.lat}&lon=${state.lon}&start_year=1900&end_year=2025&location_name=${encodeURIComponent(state.locationName)}`;
    window.open(url, "_blank");
  });

  // Print Report
  document.getElementById("btn-print-report").addEventListener("click", () => {
    window.print();
  });

  // Hourly Deluge Modal
  document.getElementById("btn-view-hourly").addEventListener("click", openHourlyModal);
  document.getElementById("btn-close-modal").addEventListener("click", () => {
    document.getElementById("modal-hourly").classList.remove("active");
  });

  // Comparison Controls
  renderComparisonTags();
  document.getElementById("btn-add-compare-year").addEventListener("click", () => {
    const input = document.getElementById("input-compare-year");
    const yr = parseInt(input.value);
    if (yr >= 1900 && yr <= 2025 && !state.comparisonYears.includes(yr)) {
      state.comparisonYears.push(yr);
      state.comparisonYears.sort((a, b) => a - b);
      input.value = "";
      renderComparisonTags();
      loadComparisonData();
    }
  });

  // Presets
  document.getElementById("preset-algiers-centennial").addEventListener("click", () => {
    state.comparisonYears = [1900, 1950, 1980, 2000, 2024];
    renderComparisonTags();
    loadComparisonData();
  });

  document.getElementById("preset-drought-cycles").addEventListener("click", () => {
    state.comparisonYears = [1921, 1945, 1983, 1994, 2020];
    renderComparisonTags();
    loadComparisonData();
  });

  document.getElementById("preset-regional-contrast").addEventListener("click", () => {
    loadRegionalComparison();
  });
}

// Switch Active Tab
function switchTab(tabId) {
  state.activeTab = tabId;
  document.querySelectorAll(".tab-btn").forEach(b => {
    b.classList.toggle("active", b.getAttribute("data-tab") === tabId);
  });
  document.querySelectorAll(".tab-content").forEach(c => {
    c.style.display = (c.id === tabId) ? "block" : "none";
  });

  if (tabId === "tab-map" && state.mapInstance) {
    setTimeout(() => {
      state.mapInstance.invalidateSize();
      loadMapDistribution();
    }, 150);
  } else if (tabId === "tab-trends") {
    loadTimelineData();
  } else if (tabId === "tab-compare") {
    loadComparisonData();
  }
}

// Set Year
function setYear(yr, refreshData = true) {
  state.currentYear = yr;
  document.getElementById("current-year-val").textContent = yr;
  document.getElementById("timeline-slider").value = yr;
  document.querySelectorAll(".card-year-tag").forEach(el => el.textContent = yr);

  // Badge GPCC vs ERA5
  const badge = document.getElementById("year-source-badge");
  if (yr < 1940) {
    badge.textContent = "GPCC";
    badge.className = "source-tag gpcc";
  } else {
    badge.textContent = "ERA5";
    badge.className = "source-tag era5";
  }

  if (refreshData) {
    loadPrecipitationYear();
    if (state.activeTab === "tab-map") {
      loadMapDistribution();
    }
  }
}

// Replay Animation Play/Pause
function togglePlay() {
  if (state.isPlaying) {
    clearInterval(state.playTimer);
    state.isPlaying = false;
    document.getElementById("play-icon").textContent = "▶";
    document.getElementById("btn-play-timeline").classList.remove("playing");
  } else {
    state.isPlaying = true;
    document.getElementById("play-icon").textContent = "⏸";
    document.getElementById("btn-play-timeline").classList.add("playing");
    state.playTimer = setInterval(() => {
      let nextYear = state.currentYear + 1;
      if (nextYear > 2025) nextYear = 1900;
      setYear(nextYear, true);
    }, 1200);
  }
}

// Load 58 Wilayas from Backend
async function loadWilayas() {
  try {
    const res = await fetch("/api/wilayas");
    const data = await res.json();
    state.wilayas = data.wilayas || [];

    const select = document.getElementById("select-wilaya");
    select.innerHTML = '<option value="">-- Choisir une Wilaya (01 à 58) --</option>';

    state.wilayas.forEach(w => {
      const opt = document.createElement("option");
      opt.value = w.code;
      opt.textContent = `${String(w.code).padStart(2, "0")} - ${w.name} (${w.name_ar})`;
      select.appendChild(opt);
    });

    // Default select Wilaya 16 (Alger)
    select.value = "16";
    onWilayaChange(16);

    select.addEventListener("change", (e) => {
      const code = parseInt(e.target.value);
      if (code) onWilayaChange(code);
    });

    document.getElementById("select-commune").addEventListener("change", (e) => {
      const communeName = e.target.value;
      if (!communeName) return;
      const w = state.selectedWilaya;
      if (!w) return;
      const c = (w.communes || []).find(x => x.name === communeName);
      if (c) {
        setLocation(c.lat, c.lon, `${c.name} (${w.name})`);
      }
    });

  } catch (err) {
    console.error("Failed to load wilayas", err);
  }
}

function onWilayaChange(code) {
  const w = state.wilayas.find(x => x.code === code);
  if (!w) return;
  state.selectedWilaya = w;

  // Populate Communes
  const communeSelect = document.getElementById("select-commune");
  communeSelect.innerHTML = `<option value="">-- Chef-lieu : ${w.name} --</option>`;
  (w.communes || []).forEach(c => {
    const opt = document.createElement("option");
    opt.value = c.name;
    opt.textContent = c.name;
    communeSelect.appendChild(opt);
  });

  setLocation(w.lat, w.lon, `${w.name} (${w.name_ar})`);
}

function setLocation(lat, lon, name) {
  state.lat = lat;
  state.lon = lon;
  state.locationName = name;

  document.getElementById("input-lat").value = lat.toFixed(3);
  document.getElementById("input-lon").value = lon.toFixed(3);

  // Update selected marker pin on map without losing national perspective on tab-map
  if (state.mapInstance) {
    updateSelectedMarker(lat, lon, name);
  }

  loadPrecipitationYear();
  loadTimelineData();
}

// Autocomplete Search
async function executeSearch(query) {
  const dropdown = document.getElementById("search-results");
  try {
    const res = await fetch(`/api/locations/search?q=${encodeURIComponent(query)}`);
    const data = await res.json();
    const results = data.results || [];

    if (results.length === 0) {
      dropdown.innerHTML = '<div style="padding: 10px; color: #718096; font-size: 12px;">Aucun résultat trouvé</div>';
      dropdown.style.display = "block";
      return;
    }

    dropdown.innerHTML = "";
    results.forEach(item => {
      const div = document.createElement("div");
      div.className = "search-item";
      div.innerHTML = `
        <div>
          <div class="search-item-title">${item.display}</div>
          <div style="font-size: 11px; color: #718096;">Zone : ${item.zone} | Alt : ${item.elevation} m</div>
        </div>
        <span class="search-item-badge">${item.type.toUpperCase()}</span>
      `;
      div.addEventListener("click", () => {
        dropdown.style.display = "none";
        document.getElementById("input-search").value = item.name;
        if (item.wilaya_code) {
          document.getElementById("select-wilaya").value = item.wilaya_code;
        }
        setLocation(item.lat, item.lon, item.display);
      });
      dropdown.appendChild(div);
    });
    dropdown.style.display = "block";

  } catch (err) {
    console.error("Search failed", err);
  }
}

// Fetch Precipitation Data for Current (lat, lon, year)
async function loadPrecipitationYear() {
  const url = `/api/precipitation?lat=${state.lat}&lon=${state.lon}&year=${state.currentYear}`;
  try {
    const res = await fetch(url);
    const data = await res.json();
    updateDashboardView(data);
  } catch (err) {
    console.error("Failed to load precipitation", err);
  }
}

// Update KPI Cards and Charts
function updateDashboardView(data) {
  // Provenance Banner
  const datasetName = data.dataset || data.source_dataset || "Copernicus ERA5 / GPCC";
  const temporalRes = data.temporal_resolution || (data.year < 1940 ? "Données mensuelles agrégées" : "Cumuls journaliers et horaires");
  const obsType = data.observation_type || (data.year < 1940 ? "Analyse pluviométrique sur grille (WMO / GPCC v2022)" : "Réanalyse atmosphérique (ECMWF ERA5 / 4D-Var)");

  document.getElementById("prov-dataset-name").textContent = datasetName;
  document.getElementById("prov-observation-desc").textContent = obsType;
  document.getElementById("prov-tech-details").textContent = 
    `Résolution : ${data.spatial_resolution || '0.1° (~9 km)'} | Grille : ${data.grid_lat || lat}°N, ${data.grid_lon || lon}°E | Pas temporel : ${temporalRes}`;

  // KPI 1: Annual Total
  document.getElementById("kpi-annual-sum").textContent = data.annual_sum_mm;

  // KPI 2: Wettest Month
  let maxMonth = { month_name: "Aucun", precipitation_mm: 0 };
  (data.monthly_data || []).forEach(m => {
    if (m.precipitation_mm > maxMonth.precipitation_mm) maxMonth = m;
  });
  document.getElementById("kpi-max-month").textContent = `${maxMonth.month_name} (${maxMonth.precipitation_mm} mm)`;

  // KPI 3: Rainy Days
  if (data.daily_hourly_available && data.rainy_days_total !== undefined) {
    document.getElementById("kpi-rainy-days").textContent = data.rainy_days_total;
    document.getElementById("kpi-rainy-sub").textContent = "Jours avec précip. >= 1.0 mm (ERA5)";
  } else {
    document.getElementById("kpi-rainy-days").textContent = "N/A";
    document.getElementById("kpi-rainy-sub").textContent = "Non mesuré en continu (GPCC mensuel)";
  }

  // KPI 4: Bioclimatic Intensity
  const annual = data.annual_sum_mm;
  let intensityClass = "Faible";
  let intensityColor = "#ed8936";
  if (annual < 100) { intensityClass = "Très faible (< 100 mm)"; intensityColor = "#e53e3e"; }
  else if (annual < 300) { intensityClass = "Faible (100-300 mm)"; intensityColor = "#ed8936"; }
  else if (annual < 600) { intensityClass = "Modéré (300-600 mm)"; intensityColor = "#ecc94b"; }
  else if (annual < 900) { intensityClass = "Élevé (600-900 mm)"; intensityColor = "#48bb78"; }
  else { intensityClass = "Très élevé (> 900 mm)"; intensityColor = "#3182ce"; }

  const badge = document.getElementById("kpi-intensity-badge");
  badge.textContent = intensityClass;
  badge.style.backgroundColor = intensityColor;
  document.getElementById("kpi-zone-text").textContent = `Localisation : ${state.locationName}`;

  // Extreme event card
  const extremeCard = document.getElementById("extreme-event-card");
  const hourlyBtn = document.getElementById("btn-view-hourly");
  if (data.wettest_day && data.wettest_day.date) {
    extremeCard.style.display = "block";
    document.getElementById("extreme-day-val").textContent = `${data.wettest_day.precip_mm} mm / jour`;
    document.getElementById("extreme-day-date").textContent = `Date : ${data.wettest_day.date}`;
    hourlyBtn.style.display = "inline-block";
    hourlyBtn.setAttribute("data-date", data.wettest_day.date);
  } else {
    document.getElementById("extreme-day-val").textContent = "Donnée journalière non disponible";
    document.getElementById("extreme-day-date").textContent = "Disponible à partir de 1940 (ERA5)";
    hourlyBtn.style.display = "none";
  }

  // Populate Monthly Table
  const tbody = document.getElementById("table-monthly-body");
  tbody.innerHTML = "";
  (data.monthly_data || []).forEach(m => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td><strong>${m.month_name}</strong></td>
      <td style="font-weight: 600; color: #2b6cb0;">${m.precipitation_mm} mm</td>
      <td>${m.rainy_days !== undefined ? m.rainy_days + ' j' : '--'}</td>
    `;
    tbody.appendChild(tr);
  });

  // Render Monthly Chart
  renderMonthlyChart(data.monthly_data);
}

// Chart.js: Monthly Bar Chart
function renderMonthlyChart(monthlyData) {
  const ctx = document.getElementById("chart-monthly").getContext("2d");
  const labels = (monthlyData || []).map(m => m.month_name);
  const values = (monthlyData || []).map(m => m.precipitation_mm);

  if (state.charts.monthly) {
    state.charts.monthly.destroy();
  }

  state.charts.monthly = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: `Précipitations ${state.currentYear} (mm)`,
        data: values,
        backgroundColor: "rgba(49, 130, 206, 0.75)",
        borderColor: "rgba(43, 108, 176, 1)",
        borderWidth: 1.5,
        borderRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: "top" },
        tooltip: {
          callbacks: {
            label: (item) => ` ${item.dataset.label}: ${item.parsed.y} mm`
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Hauteur de précipitations (mm)" }
        },
        x: {
          grid: { display: false }
        }
      }
    }
  });
}

// Load Long-Term Timeline Data (1900-2025)
async function loadTimelineData() {
  const url = `/api/precipitation/timeline?lat=${state.lat}&lon=${state.lon}&start_year=1900&end_year=2025`;
  try {
    const res = await fetch(url);
    const data = await res.json();
    state.timelineData = data;

    // Update Normals & Stats
    const stats = data.statistics || {};
    document.getElementById("trend-norm-61-90").textContent = stats.normal_1961_1990_mm;
    document.getElementById("trend-norm-91-20").textContent = stats.normal_1991_2020_mm;
    
    const shift = stats.normal_shift_pct;
    const shiftEl = document.getElementById("trend-norm-shift");
    shiftEl.textContent = `Variation : ${shift > 0 ? '+' : ''}${shift} %`;
    shiftEl.style.color = shift < 0 ? "#e53e3e" : "#38a169";

    if (stats.wettest_year) {
      document.getElementById("trend-wettest-year").textContent = stats.wettest_year.year;
      document.getElementById("trend-wettest-val").textContent = `${stats.wettest_year.value_mm} mm (Record)`;
    }
    if (stats.driest_year) {
      document.getElementById("trend-driest-year").textContent = stats.driest_year.year;
      document.getElementById("trend-driest-val").textContent = `${stats.driest_year.value_mm} mm (Déficit)`;
    }

    document.getElementById("trend-slope").textContent = `${stats.trend_per_decade_mm} mm/décennie`;
    document.getElementById("trend-direction").textContent = stats.trend_direction;

    // Anomaly on KPI 1
    if (stats.normal_1991_2020_mm) {
      const curSum = parseFloat(document.getElementById("kpi-annual-sum").textContent);
      if (!isNaN(curSum)) {
        const diff = Math.round(((curSum - stats.normal_1991_2020_mm) / stats.normal_1991_2020_mm) * 100);
        document.getElementById("kpi-anomaly-text").textContent = 
          `${diff >= 0 ? '+' : ''}${diff}% par rapport à la normale 1991-2020 (${stats.normal_1991_2020_mm} mm)`;
      }
    }

    // Render Timeline Chart
    renderTimelineChart(data);

  } catch (err) {
    console.error("Failed to load timeline", err);
  }
}

// Chart.js: 1900-2025 Timeline Mixed Chart
function renderTimelineChart(data) {
  const ctx = document.getElementById("chart-timeline").getContext("2d");
  const years = data.years || [];
  const annual = data.annual_precipitation_mm || [];
  const rolling = data.rolling_10yr_mean_mm || [];

  if (state.charts.timeline) {
    state.charts.timeline.destroy();
  }

  state.charts.timeline = new Chart(ctx, {
    type: "bar",
    data: {
      labels: years,
      datasets: [
        {
          type: "line",
          label: "Moyenne Mobile 10 ans (mm)",
          data: rolling,
          borderColor: "#e6a117",
          backgroundColor: "rgba(230, 161, 23, 0.1)",
          borderWidth: 2.5,
          tension: 0.2,
          pointRadius: 0,
          yAxisID: "y"
        },
        {
          type: "bar",
          label: "Cumul Annuel (mm)",
          data: annual,
          backgroundColor: (ctx) => {
            const yr = years[ctx.dataIndex];
            return yr < 1940 ? "rgba(43, 108, 176, 0.55)" : "rgba(47, 133, 90, 0.65)";
          },
          borderWidth: 0,
          yAxisID: "y"
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: "top" },
        tooltip: {
          callbacks: {
            label: (item) => ` ${item.dataset.label}: ${item.parsed.y} mm`
          }
        }
      },
      scales: {
        x: {
          ticks: { maxTicksLimit: 25 },
          grid: { display: false }
        },
        y: {
          beginAtZero: true,
          title: { display: true, text: "Précipitations Annuelles (mm)" }
        }
      }
    }
  });
}

// Initialize Leaflet Map
function initMap() {
  const mapElement = document.getElementById("algeria-map");
  if (!mapElement) return;

  state.mapInstance = L.map("algeria-map", {
    center: [28.2, 2.8],
    zoom: 5,
    minZoom: 4,
    maxZoom: 18
  });

  // 1. OpenStreetMap Standard (Clear, fast, no API key required)
  const osmLayer = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19
  });

  // 2. Esri World Topo Map (Relief, Topographie, Atlas mountains)
  const esriTopo = L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}", {
    attribution: 'Tiles &copy; Esri &mdash; USGS, FAO, NPS, Atlas Algérie',
    maxZoom: 18
  });

  // 3. Esri World Imagery (Satellite)
  const esriSat = L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", {
    attribution: 'Tiles &copy; Esri, Earthstar Geographics',
    maxZoom: 18
  });

  // Set OSM as default
  osmLayer.addTo(state.mapInstance);

  // Layer control switcher
  const baseLayers = {
    "🗺️ Carte Standard (OpenStreetMap)": osmLayer,
    "🏔️ Relief & Topographie (Esri Topo)": esriTopo,
    "🛰️ Vue Satellite (Esri Imagery)": esriSat
  };
  L.control.layers(baseLayers, null, { position: "topright" }).addTo(state.mapInstance);

  state.mapMarkersLayer = L.layerGroup().addTo(state.mapInstance);
  state.selectedMarkerLayer = L.layerGroup().addTo(state.mapInstance);

  // Click on map to select custom point
  state.mapInstance.on("click", (e) => {
    const lat = e.latlng.lat;
    const lon = e.latlng.lng;
    if (lat >= 19.0 && lat <= 38.0 && lon >= -9.0 && lon <= 12.5) {
      setLocation(lat, lon, `Point (${lat.toFixed(3)}°N, ${lon.toFixed(3)}°E)`);
    }
  });

  // Initial marker for current selection
  updateSelectedMarker(state.lat, state.lon, state.locationName);
}

// Update Location Pin for Current Active Point
function updateSelectedMarker(lat, lon, label) {
  if (!state.selectedMarkerLayer) return;
  state.selectedMarkerLayer.clearLayers();

  const pinIcon = L.divIcon({
    className: "current-location-marker",
    html: `<div style="background: #e53e3e; width: 18px; height: 18px; border-radius: 50%; border: 3px solid #ffffff; box-shadow: 0 0 10px rgba(229,62,62,0.8); animation: pulse 1.8s infinite;"></div>`,
    iconSize: [22, 22],
    iconAnchor: [11, 11]
  });

  const marker = L.marker([lat, lon], { icon: pinIcon, zIndexOffset: 1000 });
  marker.bindTooltip(`📍 Position sélectionnée : <strong>${label}</strong>`, {
    permanent: false,
    direction: "top"
  });
  marker.addTo(state.selectedMarkerLayer);
}

// Load Map Distribution for All 58 Wilayas
async function loadMapDistribution() {
  if (!state.mapMarkersLayer) return;
  state.mapMarkersLayer.clearLayers();

  try {
    const res = await fetch(`/api/map/distribution?year=${state.currentYear}`);
    const data = await res.json();
    const wilayas = data.wilayas || [];

    wilayas.forEach(w => {
      // Radius scaled smoothly according to precipitation
      const radius = Math.max(7, Math.min(22, Math.sqrt(w.precipitation_mm) * 0.75));
      const circle = L.circleMarker([w.lat, w.lon], {
        radius: radius,
        fillColor: w.color,
        color: "#ffffff",
        weight: 1.8,
        opacity: 0.95,
        fillOpacity: 0.85
      });

      // Hover Tooltip
      circle.bindTooltip(`
        <div style="font-family: inherit; font-size: 12px; line-height: 1.5;">
          <strong style="color: #1a365d; font-size: 13px;">${w.code.toString().padStart(2, '0')} - ${w.name} (${w.name_ar})</strong><br>
          Précipitations ${state.currentYear} : <strong style="color: #2b6cb0;">${w.precipitation_mm} mm</strong><br>
          <span style="display:inline-block; margin-top:3px; padding: 2px 7px; border-radius: 4px; background: ${w.color}; color: #ffffff; font-size: 10px; font-weight: 700;">
            ${w.intensity_fr}
          </span><br>
          <span style="color: #718096; font-size: 11px;">Étage : ${w.zone}</span>
        </div>
      `, { direction: "top", sticky: true });

      // Click Popup with Explore Button
      circle.bindPopup(`
        <div style="font-family: inherit; padding: 4px; min-width: 190px;">
          <h4 style="margin: 0 0 6px 0; color: #1a365d; font-size: 13px; border-bottom: 2px solid #e2e8f0; padding-bottom: 4px;">
            ${w.code.toString().padStart(2, '0')} - ${w.name} (${w.name_ar})
          </h4>
          <p style="margin: 3px 0; font-size: 12px;"><strong>Pluviométrie ${state.currentYear} :</strong> <span style="color: #2b6cb0; font-weight: 700;">${w.precipitation_mm} mm</span></p>
          <p style="margin: 3px 0; font-size: 12px;"><strong>Catégorie :</strong> ${w.intensity_fr}</p>
          <p style="margin: 3px 0; font-size: 12px;"><strong>Étage bioclimatique :</strong> ${w.zone}</p>
          <p style="margin: 3px 0; font-size: 11px; color: #718096;">Altitude moyenne : ${w.elevation || '--'} m</p>
          <button onclick="selectWilayaFromMap(${w.code})" style="margin-top: 8px; width: 100%; background: #2b6cb0; color: #ffffff; border: none; padding: 7px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; font-weight: 700;">
            📊 Explorer cette Wilaya
          </button>
        </div>
      `);

      circle.addTo(state.mapMarkersLayer);
    });

    // Keep active pin visible
    updateSelectedMarker(state.lat, state.lon, state.locationName);

  } catch (err) {
    console.error("Failed to load map distribution", err);
  }
}

// Window global function for popup button click
window.selectWilayaFromMap = function(code) {
  document.getElementById("select-wilaya").value = code;
  onWilayaChange(code);
  switchTab("tab-dashboard");
};

// Comparison Module
function renderComparisonTags() {
  const container = document.getElementById("compare-years-tags");
  container.innerHTML = "";
  state.comparisonYears.forEach(yr => {
    const pill = document.createElement("span");
    pill.className = "tag-pill";
    pill.innerHTML = `<span>${yr}</span> <span class="remove-tag" data-year="${yr}">&times;</span>`;
    pill.querySelector(".remove-tag").addEventListener("click", () => {
      state.comparisonYears = state.comparisonYears.filter(y => y !== yr);
      renderComparisonTags();
      loadComparisonData();
    });
    container.appendChild(pill);
  });
}

async function loadComparisonData() {
  const payload = {
    locations: [{ name: state.locationName, lat: state.lat, lon: state.lon }],
    years: state.comparisonYears
  };

  try {
    const res = await fetch("/api/compare", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const result = await res.json();
    renderComparisonChart(result);
  } catch (err) {
    console.error("Comparison request failed", err);
  }
}

async function loadRegionalComparison() {
  const payload = {
    locations: state.comparisonLocations,
    years: [state.currentYear]
  };

  try {
    const res = await fetch("/api/compare", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const result = await res.json();
    renderRegionalComparisonChart(result);
  } catch (err) {
    console.error("Regional comparison failed", err);
  }
}

function renderComparisonChart(data) {
  const ctx = document.getElementById("chart-compare").getContext("2d");
  const comp = (data.comparisons || [])[0];
  if (!comp) return;

  const years = (comp.data_by_year || []).map(d => d.year);
  const values = (comp.data_by_year || []).map(d => d.annual_sum_mm);

  if (state.charts.compare) {
    state.charts.compare.destroy();
  }

  state.charts.compare = new Chart(ctx, {
    type: "bar",
    data: {
      labels: years.map(String),
      datasets: [{
        label: `Précipitations Annuelles à ${comp.location} (mm)`,
        data: values,
        backgroundColor: [
          "#3182ce", "#48bb78", "#ecc94b", "#ed8936", "#9f7aea", "#38b2ac"
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Précipitations Cumulées (mm)" }
        }
      }
    }
  });

  // Render Table
  const tableWrapper = document.getElementById("compare-table-wrapper");
  let tableHtml = `
    <table class="data-table">
      <thead>
        <tr>
          <th>Année</th>
          <th>Précipitations (mm)</th>
          <th>Source des Données</th>
          <th>Mois le plus pluvieux</th>
        </tr>
      </thead>
      <tbody>
  `;
  (comp.data_by_year || []).forEach(d => {
    tableHtml += `
      <tr>
        <td><strong>${d.year}</strong></td>
        <td style="font-weight: 700; color: #2b6cb0;">${d.annual_sum_mm} mm</td>
        <td><span class="source-tag ${d.source === 'GPCC' ? 'gpcc' : 'era5'}">${d.dataset}</span></td>
        <td>${Math.max(...d.monthly_data)} mm</td>
      </tr>
    `;
  });
  tableHtml += "</tbody></table>";
  tableWrapper.innerHTML = tableHtml;
}

function renderRegionalComparisonChart(data) {
  const ctx = document.getElementById("chart-compare").getContext("2d");
  const comps = data.comparisons || [];
  const labels = comps.map(c => c.location);
  const values = comps.map(c => (c.data_by_year[0] ? c.data_by_year[0].annual_sum_mm : 0));

  if (state.charts.compare) {
    state.charts.compare.destroy();
  }

  state.charts.compare = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: `Comparaison Régionale (${state.currentYear}) en mm`,
        data: values,
        backgroundColor: ["#3182ce", "#48bb78", "#805ad5", "#dd6b20"],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Précipitations Annuelles (mm)" }
        }
      }
    }
  });
}

// Hourly Deluge Modal
async function openHourlyModal() {
  const btn = document.getElementById("btn-view-hourly");
  const dateStr = btn.getAttribute("data-date");
  if (!dateStr) return;

  document.getElementById("modal-hourly-title").textContent = 
    `⚡ Reconstitution Horaire de la Tempête : ${dateStr} à ${state.locationName}`;
  document.getElementById("modal-hourly").classList.add("active");

  try {
    const res = await fetch(`/api/precipitation/hourly?lat=${state.lat}&lon=${state.lon}&date=${dateStr}`);
    const data = await res.json();
    renderHourlyChart(data);
  } catch (err) {
    console.error("Failed to load hourly data", err);
  }
}

function renderHourlyChart(data) {
  const ctx = document.getElementById("chart-hourly").getContext("2d");
  const hours = (data.hourly_data || []).map(h => h.time);
  const values = (data.hourly_data || []).map(h => h.precip_mm);

  if (state.charts.hourly) {
    state.charts.hourly.destroy();
  }

  state.charts.hourly = new Chart(ctx, {
    type: "line",
    data: {
      labels: hours,
      datasets: [{
        label: `Intensité Horaire (mm/h) — Total Jour : ${data.daily_total_mm} mm`,
        data: values,
        borderColor: "#3182ce",
        backgroundColor: "rgba(49, 130, 206, 0.2)",
        fill: true,
        tension: 0.3,
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Hauteur de Pluie (mm/h)" }
        },
        x: {
          title: { display: true, text: "Heure Locale (UTC+1)" }
        }
      }
    }
  });
}
