"""
Algerian Geographic Database: 58 Wilayas, Communes, Coordinates, and Bioclimatic Classification.
Hydro-Meteorological Reference for Precipitation Analysis.
"""

from typing import List, Dict, Any, Optional

WILAYAS: List[Dict[str, Any]] = [
    {
        "code": 1,
        "name": "Adrar",
        "name_ar": "أدرار",
        "lat": 27.874,
        "lon": -0.293,
        "elevation": 276,
        "zone": "Saharan",
        "avg_annual_precip_mm": 15.2,
        "communes": [
            {"name": "Adrar", "lat": 27.874, "lon": -0.293},
            {"name": "Reggane", "lat": 26.719, "lon": 0.171},
            {"name": "Aoulef", "lat": 26.966, "lon": 1.083},
            {"name": "Zaouiet Kounta", "lat": 27.216, "lon": -0.200},
            {"name": "Fenoughil", "lat": 27.650, "lon": -0.316}
        ]
    },
    {
        "code": 2,
        "name": "Chlef",
        "name_ar": "الشلف",
        "lat": 36.165,
        "lon": 1.334,
        "elevation": 114,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 418.0,
        "communes": [
            {"name": "Chlef", "lat": 36.165, "lon": 1.334},
            {"name": "Ténès", "lat": 36.511, "lon": 1.306},
            {"name": "Boukadir", "lat": 36.066, "lon": 1.127},
            {"name": "Oued Fodda", "lat": 36.183, "lon": 1.533},
            {"name": "El Karimia", "lat": 36.116, "lon": 1.550}
        ]
    },
    {
        "code": 3,
        "name": "Laghouat",
        "name_ar": "الأغواط",
        "lat": 33.800,
        "lon": 2.865,
        "elevation": 769,
        "zone": "Arid",
        "avg_annual_precip_mm": 174.5,
        "communes": [
            {"name": "Laghouat", "lat": 33.800, "lon": 2.865},
            {"name": "Aflou", "lat": 34.116, "lon": 2.100},
            {"name": "Ksar El Hirane", "lat": 33.783, "lon": 3.133},
            {"name": "Hassi R'Mel", "lat": 32.930, "lon": 3.270}
        ]
    },
    {
        "code": 4,
        "name": "Oum El Bouaghi",
        "name_ar": "أم البواقي",
        "lat": 35.875,
        "lon": 7.113,
        "elevation": 902,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 355.0,
        "communes": [
            {"name": "Oum El Bouaghi", "lat": 35.875, "lon": 7.113},
            {"name": "Aïn Beïda", "lat": 35.796, "lon": 7.392},
            {"name": "Aïn M'lila", "lat": 36.033, "lon": 6.583},
            {"name": "Meskiana", "lat": 35.633, "lon": 7.666}
        ]
    },
    {
        "code": 5,
        "name": "Batna",
        "name_ar": "باتنة",
        "lat": 35.556,
        "lon": 6.174,
        "elevation": 1048,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 362.0,
        "communes": [
            {"name": "Batna", "lat": 35.556, "lon": 6.174},
            {"name": "Barika", "lat": 35.389, "lon": 5.365},
            {"name": "Aïn Touta", "lat": 35.383, "lon": 5.900},
            {"name": "Merouana", "lat": 35.633, "lon": 5.911},
            {"name": "Arris", "lat": 35.260, "lon": 6.502}
        ]
    },
    {
        "code": 6,
        "name": "Béjaïa",
        "name_ar": "بجاية",
        "lat": 36.751,
        "lon": 5.056,
        "elevation": 110,
        "zone": "Humid",
        "avg_annual_precip_mm": 845.0,
        "communes": [
            {"name": "Béjaïa", "lat": 36.751, "lon": 5.056},
            {"name": "Akbou", "lat": 36.457, "lon": 4.542},
            {"name": "Amizour", "lat": 36.643, "lon": 4.904},
            {"name": "Kherrata", "lat": 36.493, "lon": 5.279},
            {"name": "Sidi Aïch", "lat": 36.611, "lon": 4.690},
            {"name": "Aokas", "lat": 36.637, "lon": 5.244}
        ]
    },
    {
        "code": 7,
        "name": "Biskra",
        "name_ar": "بسكرة",
        "lat": 34.850,
        "lon": 5.733,
        "elevation": 128,
        "zone": "Arid",
        "avg_annual_precip_mm": 156.0,
        "communes": [
            {"name": "Biskra", "lat": 34.850, "lon": 5.733},
            {"name": "Tolga", "lat": 34.722, "lon": 5.378},
            {"name": "Sidi Okba", "lat": 34.750, "lon": 5.898},
            {"name": "Zeribet El Oued", "lat": 34.683, "lon": 6.516}
        ]
    },
    {
        "code": 8,
        "name": "Béchar",
        "name_ar": "بشار",
        "lat": 31.616,
        "lon": -2.216,
        "elevation": 773,
        "zone": "Saharan",
        "avg_annual_precip_mm": 88.0,
        "communes": [
            {"name": "Béchar", "lat": 31.616, "lon": -2.216},
            {"name": "Kenadsa", "lat": 31.560, "lon": -2.420},
            {"name": "Abadla", "lat": 31.016, "lon": -2.733},
            {"name": "Taghit", "lat": 30.916, "lon": -2.030}
        ]
    },
    {
        "code": 9,
        "name": "Blida",
        "name_ar": "البليدة",
        "lat": 36.470,
        "lon": 2.828,
        "elevation": 260,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 740.0,
        "communes": [
            {"name": "Blida", "lat": 36.470, "lon": 2.828},
            {"name": "Boufarik", "lat": 36.575, "lon": 2.913},
            {"name": "El Affroun", "lat": 36.467, "lon": 2.633},
            {"name": "Chréa", "lat": 36.425, "lon": 2.876},
            {"name": "Larbaa", "lat": 36.564, "lon": 3.155}
        ]
    },
    {
        "code": 10,
        "name": "Bouira",
        "name_ar": "البويرة",
        "lat": 36.375,
        "lon": 3.900,
        "elevation": 557,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 620.0,
        "communes": [
            {"name": "Bouira", "lat": 36.375, "lon": 3.900},
            {"name": "Lakhdaria", "lat": 36.564, "lon": 3.593},
            {"name": "Sour El Ghozlane", "lat": 36.147, "lon": 3.691},
            {"name": "M'Chedallah", "lat": 36.368, "lon": 4.282},
            {"name": "Aïn Bessem", "lat": 36.293, "lon": 3.673}
        ]
    },
    {
        "code": 11,
        "name": "Tamanrasset",
        "name_ar": "تمنراست",
        "lat": 22.785,
        "lon": 5.522,
        "elevation": 1377,
        "zone": "Saharan",
        "avg_annual_precip_mm": 54.0,
        "communes": [
            {"name": "Tamanrasset", "lat": 22.785, "lon": 5.522},
            {"name": "Abalessa", "lat": 22.895, "lon": 4.856},
            {"name": "Idlès", "lat": 23.824, "lon": 5.932},
            {"name": "Tazrouk", "lat": 23.424, "lon": 6.273}
        ]
    },
    {
        "code": 12,
        "name": "Tébessa",
        "name_ar": "تبسة",
        "lat": 35.404,
        "lon": 8.124,
        "elevation": 858,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 352.0,
        "communes": [
            {"name": "Tébessa", "lat": 35.404, "lon": 8.124},
            {"name": "Cheria", "lat": 35.272, "lon": 7.753},
            {"name": "El Ouenza", "lat": 35.966, "lon": 8.350},
            {"name": "Bir El Ater", "lat": 34.750, "lon": 8.060}
        ]
    },
    {
        "code": 13,
        "name": "Tlemcen",
        "name_ar": "تلمسان",
        "lat": 34.878,
        "lon": -1.315,
        "elevation": 820,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 485.0,
        "communes": [
            {"name": "Tlemcen", "lat": 34.878, "lon": -1.315},
            {"name": "Maghnia", "lat": 34.808, "lon": -1.733},
            {"name": "Ghazaouet", "lat": 35.097, "lon": -1.857},
            {"name": "Remchi", "lat": 35.061, "lon": -1.433},
            {"name": "Sebdou", "lat": 34.636, "lon": -1.334}
        ]
    },
    {
        "code": 14,
        "name": "Tiaret",
        "name_ar": "تيارت",
        "lat": 35.371,
        "lon": 1.316,
        "elevation": 995,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 395.0,
        "communes": [
            {"name": "Tiaret", "lat": 35.371, "lon": 1.316},
            {"name": "Sougueur", "lat": 35.185, "lon": 1.496},
            {"name": "Frenda", "lat": 35.065, "lon": 1.049},
            {"name": "Ksar Chellala", "lat": 35.215, "lon": 2.318},
            {"name": "Mahdia", "lat": 35.503, "lon": 1.761}
        ]
    },
    {
        "code": 15,
        "name": "Tizi Ouzou",
        "name_ar": "تيزي وزو",
        "lat": 36.711,
        "lon": 4.045,
        "elevation": 200,
        "zone": "Humid",
        "avg_annual_precip_mm": 860.0,
        "communes": [
            {"name": "Tizi Ouzou", "lat": 36.711, "lon": 4.045},
            {"name": "Azazga", "lat": 36.745, "lon": 4.372},
            {"name": "Draa El Mizan", "lat": 36.533, "lon": 3.833},
            {"name": "Tigzirt", "lat": 36.889, "lon": 4.120},
            {"name": "Larbaa Nath Irathen", "lat": 36.634, "lon": 4.204},
            {"name": "Aïn El Hammam", "lat": 36.564, "lon": 4.306}
        ]
    },
    {
        "code": 16,
        "name": "Alger",
        "name_ar": "الجزائر",
        "lat": 36.7538,
        "lon": 3.0588,
        "elevation": 50,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 670.0,
        "communes": [
            {"name": "Alger Centre", "lat": 36.775, "lon": 3.060},
            {"name": "Bab El Oued", "lat": 36.790, "lon": 3.050},
            {"name": "Hydra", "lat": 36.743, "lon": 3.042},
            {"name": "Dar El Beïda", "lat": 36.713, "lon": 3.212},
            {"name": "Rouïba", "lat": 36.733, "lon": 3.283},
            {"name": "Zéralda", "lat": 36.716, "lon": 2.842},
            {"name": "Bir Mourad Raïs", "lat": 36.735, "lon": 3.051},
            {"name": "El Harrach", "lat": 36.720, "lon": 3.136}
        ]
    },
    {
        "code": 17,
        "name": "Djelfa",
        "name_ar": "الجلفة",
        "lat": 34.672,
        "lon": 3.263,
        "elevation": 1138,
        "zone": "Arid",
        "avg_annual_precip_mm": 310.0,
        "communes": [
            {"name": "Djelfa", "lat": 34.672, "lon": 3.263},
            {"name": "Aïn Oussara", "lat": 35.451, "lon": 2.906},
            {"name": "Messaad", "lat": 34.161, "lon": 3.503},
            {"name": "Birine", "lat": 35.633, "lon": 3.216},
            {"name": "Hassi Bahbah", "lat": 35.080, "lon": 3.030}
        ]
    },
    {
        "code": 18,
        "name": "Jijel",
        "name_ar": "جيجل",
        "lat": 36.820,
        "lon": 5.766,
        "elevation": 45,
        "zone": "Humid",
        "avg_annual_precip_mm": 1050.0,
        "communes": [
            {"name": "Jijel", "lat": 36.820, "lon": 5.766},
            {"name": "Taher", "lat": 36.772, "lon": 5.897},
            {"name": "El Milia", "lat": 36.751, "lon": 6.264},
            {"name": "Ziama Mansouriah", "lat": 36.674, "lon": 5.483},
            {"name": "El Ancer", "lat": 36.790, "lon": 6.130}
        ]
    },
    {
        "code": 19,
        "name": "Sétif",
        "name_ar": "سطيف",
        "lat": 36.191,
        "lon": 5.413,
        "elevation": 1096,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 415.0,
        "communes": [
            {"name": "Sétif", "lat": 36.191, "lon": 5.413},
            {"name": "El Eulma", "lat": 36.153, "lon": 5.690},
            {"name": "Aïn Oulmene", "lat": 35.918, "lon": 5.297},
            {"name": "Aïn Arnat", "lat": 36.183, "lon": 5.316},
            {"name": "Bougaa", "lat": 36.333, "lon": 5.083}
        ]
    },
    {
        "code": 20,
        "name": "Saïda",
        "name_ar": "سعيدة",
        "lat": 34.830,
        "lon": 0.151,
        "elevation": 860,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 370.0,
        "communes": [
            {"name": "Saïda", "lat": 34.830, "lon": 0.151},
            {"name": "Youb", "lat": 34.933, "lon": -0.166},
            {"name": "Hassasna", "lat": 34.816, "lon": 0.316},
            {"name": "Ouled Brahim", "lat": 34.783, "lon": 0.050}
        ]
    },
    {
        "code": 21,
        "name": "Skikda",
        "name_ar": "سكيكدة",
        "lat": 36.879,
        "lon": 6.906,
        "elevation": 25,
        "zone": "Humid",
        "avg_annual_precip_mm": 790.0,
        "communes": [
            {"name": "Skikda", "lat": 36.879, "lon": 6.906},
            {"name": "Collo", "lat": 37.008, "lon": 6.560},
            {"name": "Azzaba", "lat": 36.741, "lon": 7.106},
            {"name": "El Harrouch", "lat": 36.732, "lon": 6.840},
            {"name": "Tamalous", "lat": 36.833, "lon": 6.633}
        ]
    },
    {
        "code": 22,
        "name": "Sidi Bel Abbès",
        "name_ar": "سيدي بلعباس",
        "lat": 35.190,
        "lon": -0.630,
        "elevation": 470,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 390.0,
        "communes": [
            {"name": "Sidi Bel Abbès", "lat": 35.190, "lon": -0.630},
            {"name": "Telagh", "lat": 34.783, "lon": -0.566},
            {"name": "Sfier", "lat": 35.250, "lon": -0.550},
            {"name": "Ben Badis", "lat": 35.183, "lon": -0.766}
        ]
    },
    {
        "code": 23,
        "name": "Annaba",
        "name_ar": "عنابة",
        "lat": 36.900,
        "lon": 7.766,
        "elevation": 15,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 680.0,
        "communes": [
            {"name": "Annaba", "lat": 36.900, "lon": 7.766},
            {"name": "El Bouni", "lat": 36.866, "lon": 7.733},
            {"name": "El Hadjar", "lat": 36.800, "lon": 7.733},
            {"name": "Berrahal", "lat": 36.833, "lon": 7.450},
            {"name": "Seraïdi", "lat": 36.916, "lon": 7.666}
        ]
    },
    {
        "code": 24,
        "name": "Guelma",
        "name_ar": "قالمة",
        "lat": 36.462,
        "lon": 7.426,
        "elevation": 290,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 610.0,
        "communes": [
            {"name": "Guelma", "lat": 36.462, "lon": 7.426},
            {"name": "Oued Zenati", "lat": 36.316, "lon": 7.166},
            {"name": "Bouchegouf", "lat": 36.466, "lon": 7.716},
            {"name": "Héliopolis", "lat": 36.500, "lon": 7.450}
        ]
    },
    {
        "code": 25,
        "name": "Constantine",
        "name_ar": "قسنطينة",
        "lat": 36.365,
        "lon": 6.614,
        "elevation": 687,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 540.0,
        "communes": [
            {"name": "Constantine", "lat": 36.365, "lon": 6.614},
            {"name": "El Khroub", "lat": 36.262, "lon": 6.694},
            {"name": "Hamma Bouziane", "lat": 36.416, "lon": 6.600},
            {"name": "Ali Mendjeli", "lat": 36.242, "lon": 6.570},
            {"name": "Zighoud Youcef", "lat": 36.533, "lon": 6.716}
        ]
    },
    {
        "code": 26,
        "name": "Médéa",
        "name_ar": "المدية",
        "lat": 36.264,
        "lon": 2.754,
        "elevation": 940,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 670.0,
        "communes": [
            {"name": "Médéa", "lat": 36.264, "lon": 2.754},
            {"name": "Berrouaghia", "lat": 36.136, "lon": 2.916},
            {"name": "Ksar Boukhari", "lat": 35.887, "lon": 2.750},
            {"name": "Beni Slimane", "lat": 36.216, "lon": 3.300}
        ]
    },
    {
        "code": 27,
        "name": "Mostaganem",
        "name_ar": "مستغانم",
        "lat": 35.931,
        "lon": 0.089,
        "elevation": 104,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 375.0,
        "communes": [
            {"name": "Mostaganem", "lat": 35.931, "lon": 0.089},
            {"name": "Ain Tedeles", "lat": 35.983, "lon": 0.300},
            {"name": "Sidi Ali", "lat": 36.166, "lon": 0.416},
            {"name": "Mesra", "lat": 35.866, "lon": 0.166}
        ]
    },
    {
        "code": 28,
        "name": "M'Sila",
        "name_ar": "المسيلة",
        "lat": 35.705,
        "lon": 4.541,
        "elevation": 471,
        "zone": "Arid",
        "avg_annual_precip_mm": 235.0,
        "communes": [
            {"name": "M'Sila", "lat": 35.705, "lon": 4.541},
            {"name": "Bou Saâda", "lat": 35.214, "lon": 4.175},
            {"name": "Sidi Aïssa", "lat": 35.883, "lon": 3.766},
            {"name": "Magra", "lat": 35.600, "lon": 5.066}
        ]
    },
    {
        "code": 29,
        "name": "Mascara",
        "name_ar": "معسكر",
        "lat": 35.396,
        "lon": 0.140,
        "elevation": 590,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 430.0,
        "communes": [
            {"name": "Mascara", "lat": 35.396, "lon": 0.140},
            {"name": "Sig", "lat": 35.530, "lon": -0.190},
            {"name": "Mohammadia", "lat": 35.589, "lon": 0.067},
            {"name": "Tighennif", "lat": 35.416, "lon": 0.333}
        ]
    },
    {
        "code": 30,
        "name": "Ouargla",
        "name_ar": "ورقلة",
        "lat": 31.953,
        "lon": 5.325,
        "elevation": 138,
        "zone": "Saharan",
        "avg_annual_precip_mm": 49.0,
        "communes": [
            {"name": "Ouargla", "lat": 31.953, "lon": 5.325},
            {"name": "Hassi Messaoud", "lat": 31.680, "lon": 6.072},
            {"name": "Rouissat", "lat": 31.920, "lon": 5.350},
            {"name": "N'Goussa", "lat": 32.140, "lon": 5.300}
        ]
    },
    {
        "code": 31,
        "name": "Oran",
        "name_ar": "وهران",
        "lat": 35.698,
        "lon": -0.633,
        "elevation": 85,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 378.0,
        "communes": [
            {"name": "Oran Centre", "lat": 35.698, "lon": -0.633},
            {"name": "Es Senia", "lat": 35.648, "lon": -0.622},
            {"name": "Bir El Djir", "lat": 35.716, "lon": -0.566},
            {"name": "Arzew", "lat": 35.850, "lon": -0.316},
            {"name": "Aïn El Turk", "lat": 35.744, "lon": -0.755}
        ]
    },
    {
        "code": 32,
        "name": "El Bayadh",
        "name_ar": "البيض",
        "lat": 33.683,
        "lon": 1.019,
        "elevation": 1304,
        "zone": "Arid",
        "avg_annual_precip_mm": 270.0,
        "communes": [
            {"name": "El Bayadh", "lat": 33.683, "lon": 1.019},
            {"name": "Rogassa", "lat": 33.966, "lon": 1.100},
            {"name": "Brezina", "lat": 33.100, "lon": 1.266},
            {"name": "Labiodh Sidi Cheikh", "lat": 32.890, "lon": 0.950}
        ]
    },
    {
        "code": 33,
        "name": "Illizi",
        "name_ar": "إليزي",
        "lat": 26.483,
        "lon": 8.466,
        "elevation": 560,
        "zone": "Saharan",
        "avg_annual_precip_mm": 22.0,
        "communes": [
            {"name": "Illizi", "lat": 26.483, "lon": 8.466},
            {"name": "In Amenas", "lat": 28.033, "lon": 9.566},
            {"name": "Bordj Omar Driss", "lat": 28.800, "lon": 6.800}
        ]
    },
    {
        "code": 34,
        "name": "Bordj Bou Arréridj",
        "name_ar": "برج بوعريريج",
        "lat": 36.073,
        "lon": 4.761,
        "elevation": 928,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 405.0,
        "communes": [
            {"name": "Bordj Bou Arréridj", "lat": 36.073, "lon": 4.761},
            {"name": "Ras El Oued", "lat": 35.944, "lon": 5.031},
            {"name": "Mansoura", "lat": 36.083, "lon": 4.500},
            {"name": "Bordj Zemoura", "lat": 36.266, "lon": 4.850}
        ]
    },
    {
        "code": 35,
        "name": "Boumerdès",
        "name_ar": "بومرداس",
        "lat": 36.766,
        "lon": 3.477,
        "elevation": 40,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 710.0,
        "communes": [
            {"name": "Boumerdès", "lat": 36.766, "lon": 3.477},
            {"name": "Dellys", "lat": 36.916, "lon": 3.916},
            {"name": "Khemis El Khechna", "lat": 36.650, "lon": 3.333},
            {"name": "Boudouaou", "lat": 36.733, "lon": 3.400},
            {"name": "Zemmouri", "lat": 36.783, "lon": 3.600}
        ]
    },
    {
        "code": 36,
        "name": "El Tarf",
        "name_ar": "الطارف",
        "lat": 36.767,
        "lon": 8.313,
        "elevation": 30,
        "zone": "Humid",
        "avg_annual_precip_mm": 910.0,
        "communes": [
            {"name": "El Tarf", "lat": 36.767, "lon": 8.313},
            {"name": "El Kala", "lat": 36.895, "lon": 8.443},
            {"name": "Ben M'Hidi", "lat": 36.766, "lon": 7.900},
            {"name": "Drean", "lat": 36.683, "lon": 7.750}
        ]
    },
    {
        "code": 37,
        "name": "Tindouf",
        "name_ar": "تندوف",
        "lat": 27.671,
        "lon": -8.147,
        "elevation": 404,
        "zone": "Saharan",
        "avg_annual_precip_mm": 44.0,
        "communes": [
            {"name": "Tindouf", "lat": 27.671, "lon": -8.147},
            {"name": "Oum El Assel", "lat": 28.533, "lon": -7.033}
        ]
    },
    {
        "code": 38,
        "name": "Tissemsilt",
        "name_ar": "تيسمسيلت",
        "lat": 35.607,
        "lon": 1.810,
        "elevation": 849,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 450.0,
        "communes": [
            {"name": "Tissemsilt", "lat": 35.607, "lon": 1.810},
            {"name": "Theniet El Had", "lat": 35.866, "lon": 2.033},
            {"name": "Bordj Bounaama", "lat": 35.850, "lon": 1.633},
            {"name": "Lardjem", "lat": 35.733, "lon": 1.650}
        ]
    },
    {
        "code": 39,
        "name": "El Oued",
        "name_ar": "الوادي",
        "lat": 33.368,
        "lon": 6.867,
        "elevation": 80,
        "zone": "Saharan",
        "avg_annual_precip_mm": 72.0,
        "communes": [
            {"name": "El Oued", "lat": 33.368, "lon": 6.867},
            {"name": "Guemar", "lat": 33.495, "lon": 6.797},
            {"name": "Robbah", "lat": 33.283, "lon": 6.833},
            {"name": "Debila", "lat": 33.516, "lon": 6.950}
        ]
    },
    {
        "code": 40,
        "name": "Khenchela",
        "name_ar": "خنشلة",
        "lat": 35.435,
        "lon": 7.143,
        "elevation": 1120,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 420.0,
        "communes": [
            {"name": "Khenchela", "lat": 35.435, "lon": 7.143},
            {"name": "Kais", "lat": 35.500, "lon": 6.933},
            {"name": "Chechar", "lat": 35.100, "lon": 7.033},
            {"name": "Bouhmama", "lat": 35.333, "lon": 6.666}
        ]
    },
    {
        "code": 41,
        "name": "Souk Ahras",
        "name_ar": "سوق أهراس",
        "lat": 36.286,
        "lon": 7.951,
        "elevation": 670,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 650.0,
        "communes": [
            {"name": "Souk Ahras", "lat": 36.286, "lon": 7.951},
            {"name": "Sedrata", "lat": 36.128, "lon": 7.533},
            {"name": "M'Daourouch", "lat": 36.083, "lon": 7.733},
            {"name": "Taoura", "lat": 36.166, "lon": 8.050}
        ]
    },
    {
        "code": 42,
        "name": "Tipaza",
        "name_ar": "تيبازة",
        "lat": 36.589,
        "lon": 2.447,
        "elevation": 30,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 660.0,
        "communes": [
            {"name": "Tipaza", "lat": 36.589, "lon": 2.447},
            {"name": "Cherchell", "lat": 36.608, "lon": 2.189},
            {"name": "Kolea", "lat": 36.638, "lon": 2.768},
            {"name": "Hadjout", "lat": 36.516, "lon": 2.416},
            {"name": "Bou Ismaïl", "lat": 36.643, "lon": 2.690}
        ]
    },
    {
        "code": 43,
        "name": "Mila",
        "name_ar": "ميلة",
        "lat": 36.450,
        "lon": 6.264,
        "elevation": 465,
        "zone": "Sub-humid",
        "avg_annual_precip_mm": 620.0,
        "communes": [
            {"name": "Mila", "lat": 36.450, "lon": 6.264},
            {"name": "Chelghoum Laid", "lat": 36.166, "lon": 6.166},
            {"name": "Ferdjioua", "lat": 36.366, "lon": 5.966},
            {"name": "Tadjenanet", "lat": 36.116, "lon": 5.983}
        ]
    },
    {
        "code": 44,
        "name": "Aïn Defla",
        "name_ar": "عين الدفلى",
        "lat": 36.265,
        "lon": 1.967,
        "elevation": 280,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 510.0,
        "communes": [
            {"name": "Aïn Defla", "lat": 36.265, "lon": 1.967},
            {"name": "Khemis Miliana", "lat": 36.261, "lon": 2.220},
            {"name": "Miliana", "lat": 36.300, "lon": 2.233},
            {"name": "El Attaf", "lat": 36.224, "lon": 1.671}
        ]
    },
    {
        "code": 45,
        "name": "Naâma",
        "name_ar": "النعامة",
        "lat": 33.266,
        "lon": -0.316,
        "elevation": 1176,
        "zone": "Arid",
        "avg_annual_precip_mm": 210.0,
        "communes": [
            {"name": "Naâma", "lat": 33.266, "lon": -0.316},
            {"name": "Mecheria", "lat": 33.533, "lon": -0.283},
            {"name": "Aïn Sefra", "lat": 32.750, "lon": -0.583},
            {"name": "Tiout", "lat": 32.766, "lon": -0.416}
        ]
    },
    {
        "code": 46,
        "name": "Aïn Témouchent",
        "name_ar": "عين تموشنت",
        "lat": 35.297,
        "lon": -1.140,
        "elevation": 248,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 390.0,
        "communes": [
            {"name": "Aïn Témouchent", "lat": 35.297, "lon": -1.140},
            {"name": "Béni Saf", "lat": 35.301, "lon": -1.382},
            {"name": "Hammam Bou Hadjar", "lat": 35.378, "lon": -0.966},
            {"name": "El Malah", "lat": 35.392, "lon": -1.092}
        ]
    },
    {
        "code": 47,
        "name": "Ghardaïa",
        "name_ar": "غرداية",
        "lat": 32.490,
        "lon": 3.673,
        "elevation": 470,
        "zone": "Saharan",
        "avg_annual_precip_mm": 80.0,
        "communes": [
            {"name": "Ghardaïa", "lat": 32.490, "lon": 3.673},
            {"name": "Metlili", "lat": 32.266, "lon": 3.633},
            {"name": "El Guerara", "lat": 32.783, "lon": 4.483},
            {"name": "Berriane", "lat": 32.833, "lon": 3.766},
            {"name": "Beni Isguen", "lat": 32.476, "lon": 3.693}
        ]
    },
    {
        "code": 48,
        "name": "Relizane",
        "name_ar": "غليزان",
        "lat": 35.740,
        "lon": 0.555,
        "elevation": 67,
        "zone": "Semi-arid",
        "avg_annual_precip_mm": 390.0,
        "communes": [
            {"name": "Relizane", "lat": 35.740, "lon": 0.555},
            {"name": "Oued Rhiou", "lat": 35.961, "lon": 0.918},
            {"name": "Mazouna", "lat": 36.126, "lon": 0.875},
            {"name": "Yellel", "lat": 35.719, "lon": 0.355}
        ]
    },
    {
        "code": 49,
        "name": "Timimoun",
        "name_ar": "تيميمون",
        "lat": 29.263,
        "lon": 0.231,
        "elevation": 288,
        "zone": "Saharan",
        "avg_annual_precip_mm": 18.0,
        "communes": [
            {"name": "Timimoun", "lat": 29.263, "lon": 0.231},
            {"name": "Charouine", "lat": 29.016, "lon": -0.266},
            {"name": "Aougrout", "lat": 28.750, "lon": 0.233}
        ]
    },
    {
        "code": 50,
        "name": "Bordj Badji Mokhtar",
        "name_ar": "برج باجي مختار",
        "lat": 21.328,
        "lon": 0.954,
        "elevation": 401,
        "zone": "Hyper-arid",
        "avg_annual_precip_mm": 32.0,
        "communes": [
            {"name": "Bordj Badji Mokhtar", "lat": 21.328, "lon": 0.954},
            {"name": "Timiaouine", "lat": 20.433, "lon": 1.816}
        ]
    },
    {
        "code": 51,
        "name": "Ouled Djellal",
        "name_ar": "أولاد جلال",
        "lat": 34.427,
        "lon": 5.065,
        "elevation": 185,
        "zone": "Arid",
        "avg_annual_precip_mm": 138.0,
        "communes": [
            {"name": "Ouled Djellal", "lat": 34.427, "lon": 5.065},
            {"name": "Sidi Khaled", "lat": 34.383, "lon": 4.983},
            {"name": "Ras El Miaad", "lat": 34.250, "lon": 4.516}
        ]
    },
    {
        "code": 52,
        "name": "Béni Abbès",
        "name_ar": "بني عباس",
        "lat": 30.133,
        "lon": -2.166,
        "elevation": 483,
        "zone": "Saharan",
        "avg_annual_precip_mm": 41.0,
        "communes": [
            {"name": "Béni Abbès", "lat": 30.133, "lon": -2.166},
            {"name": "Kerzaz", "lat": 29.450, "lon": -1.416},
            {"name": "Igli", "lat": 30.500, "lon": -2.183},
            {"name": "El Ouata", "lat": 29.866, "lon": -1.833}
        ]
    },
    {
        "code": 53,
        "name": "In Salah",
        "name_ar": "عين صالح",
        "lat": 27.193,
        "lon": 2.460,
        "elevation": 273,
        "zone": "Hyper-arid",
        "avg_annual_precip_mm": 16.5,
        "communes": [
            {"name": "In Salah", "lat": 27.193, "lon": 2.460},
            {"name": "In Ghar", "lat": 27.100, "lon": 1.916},
            {"name": "Foggaret Ezzaouia", "lat": 27.466, "lon": 2.766}
        ]
    },
    {
        "code": 54,
        "name": "In Guezzam",
        "name_ar": "عين قزام",
        "lat": 19.570,
        "lon": 5.769,
        "elevation": 402,
        "zone": "Saharan",
        "avg_annual_precip_mm": 45.0,
        "communes": [
            {"name": "In Guezzam", "lat": 19.570, "lon": 5.769},
            {"name": "Tin Zaouatine", "lat": 19.954, "lon": 2.966}
        ]
    },
    {
        "code": 55,
        "name": "Touggourt",
        "name_ar": "تقرت",
        "lat": 33.105,
        "lon": 6.058,
        "elevation": 68,
        "zone": "Saharan",
        "avg_annual_precip_mm": 60.0,
        "communes": [
            {"name": "Touggourt", "lat": 33.105, "lon": 6.058},
            {"name": "Temacine", "lat": 33.016, "lon": 6.033},
            {"name": "Megarine", "lat": 33.183, "lon": 6.083},
            {"name": "Taibet", "lat": 33.083, "lon": 6.533}
        ]
    },
    {
        "code": 56,
        "name": "Djanet",
        "name_ar": "جانت",
        "lat": 24.554,
        "lon": 9.485,
        "elevation": 1053,
        "zone": "Saharan",
        "avg_annual_precip_mm": 18.0,
        "communes": [
            {"name": "Djanet", "lat": 24.554, "lon": 9.485},
            {"name": "Bordj El Haouas", "lat": 24.883, "lon": 8.466}
        ]
    },
    {
        "code": 57,
        "name": "El M'Ghair",
        "name_ar": "المغير",
        "lat": 33.950,
        "lon": 5.923,
        "elevation": -12,
        "zone": "Saharan",
        "avg_annual_precip_mm": 68.0,
        "communes": [
            {"name": "El M'Ghair", "lat": 33.950, "lon": 5.923},
            {"name": "Djamaa", "lat": 33.533, "lon": 5.983},
            {"name": "Sidi Khelil", "lat": 34.016, "lon": 5.966}
        ]
    },
    {
        "code": 58,
        "name": "El Meniaa",
        "name_ar": "المنيعة",
        "lat": 30.585,
        "lon": 2.879,
        "elevation": 395,
        "zone": "Saharan",
        "avg_annual_precip_mm": 35.0,
        "communes": [
            {"name": "El Meniaa", "lat": 30.585, "lon": 2.879},
            {"name": "Hassi Gara", "lat": 30.516, "lon": 2.916}
        ]
    }
]

# Lookup dictionary by code
WILAYAS_BY_CODE = {w["code"]: w for w in WILAYAS}

def search_locations(query: str, limit: int = 15) -> List[Dict[str, Any]]:
    """Search Wilayas and Communes by query string."""
    q = query.strip().lower()
    if not q:
        return []
    
    results = []
    # Match Wilayas
    for w in WILAYAS:
        if q in w["name"].lower() or q in w["name_ar"] or str(w["code"]) == q:
            results.append({
                "type": "wilaya",
                "wilaya_code": w["code"],
                "name": w["name"],
                "name_ar": w["name_ar"],
                "display": f"{w['code']:02d} - {w['name']} ({w['name_ar']})",
                "lat": w["lat"],
                "lon": w["lon"],
                "zone": w["zone"],
                "elevation": w["elevation"]
            })
            if len(results) >= limit:
                return results

    # Match Communes
    for w in WILAYAS:
        for c in w.get("communes", []):
            if q in c["name"].lower():
                results.append({
                    "type": "commune",
                    "wilaya_code": w["code"],
                    "wilaya_name": w["name"],
                    "name": c["name"],
                    "display": f"{c['name']} (Wilaya de {w['name']})",
                    "lat": c["lat"],
                    "lon": c["lon"],
                    "zone": w["zone"],
                    "elevation": w.get("elevation", 0)
                })
                if len(results) >= limit:
                    return results

    return results

def find_nearest_wilaya(lat: float, lon: float) -> Dict[str, Any]:
    """Find the nearest wilaya center to the given coordinates."""
    import math
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0 # km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) ** 2 +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) ** 2)
        return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    closest = None
    min_dist = float("inf")
    for w in WILAYAS:
        d = haversine(lat, lon, w["lat"], w["lon"])
        if d < min_dist:
            min_dist = d
            closest = w
    return {"wilaya": closest, "distance_km": round(min_dist, 1)}
