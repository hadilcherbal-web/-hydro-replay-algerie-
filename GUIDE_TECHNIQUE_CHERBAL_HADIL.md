# 📘 GUIDE TECHNIQUE & FICHE MÉMO TECHNIQUE
### Projet : **HYDRO-REPLAY ALGÉRIE (1900 – 2025)**
**Présenté par :** Ingénieure d'État en Hydraulique **CHERBAL Hadil**  
**Spécialité :** Hydraulique & Gestion des Ressources en Eau  
**Plateforme Déployée :** [hydro-replay-algerie-1.onrender.com](https://hydro-replay-algerie-1.onrender.com)  
**Code d'accès sécurisé :** `2005`

---

## 🎯 1. Les Réponses Clés à Mémoriser pour le Professeur

### Q1 : Pourquoi la couleur change entre Bleu (1900-1939) et Vert (1940-2025) ?
> **Réponse technique :**  
> *"Monsieur le Professeur, ce changement de couleur traduit la rigueur scientifique de la plateforme en distinguant la source de données :"*
> - **Bleu (1900 – 1939) : Données GPCC v2022 (Global Precipitation Climatology Centre)** de l'Organisation Météorologique Mondiale (OMM / DWD). Analyse par grille basée sur les observations réelles des stations pluviométriques in-situ historiques, avec une résolution spatiale de **0.5° (~50 km)** et une agrégation **mensuelle**.
> - **Vert (1940 – 2025) : Réanalyse atmosphérique physique Copernicus ERA5-Land (ECMWF)**. Modèle physique de réanalyse globale haute précision, avec une résolution spatiale fine de **0.1° (~9 km)** et une maille continue intégrant le bilan hydrologique physique.

---

### Q2 : Est-ce que le comparateur ne compare que 4 wilayas (Alger, Oran, Constantine, Ouargla) ?
> **Réponse technique :**  
> *"Absolument pas ! La plateforme couvre **l'intégralité des 58 Wilayas d'Algérie** (de 01 Adrar à 58 In Guezzam)."*  
> *"Le bouton 'Alger vs Oran vs Constantine vs Ouargla' est simplement un **préréglage rapide (Preset)** conçu pour démontrer instantanément au jury le contraste des 4 grands gradients bioclimatiques de l'Algérie :"*
> 1. **Alger :** Climat méditerranéen subhumide côtier.
> 2. **Constantine :** Région des hauts plateaux de l'Est à forte variabilité.
> 3. **Oran :** Région Ouest marquée par un déficit pluviométrique structurel.
> 4. **Ouargla :** Étage saharien hyper-aride.
>
> *L'ingénieur peut sélectionner n'importe quelle wilaya parmi les 58 et n'importe quelle année entre 1900 et 2025 pour une analyse comparative personnalisée.*

---

### Q3 : Pourquoi voit-on "N/A" pour les "Jours de pluie" avant 1940 ?
> **Réponse technique :**  
> *"Le symbole **N/A** signifie **Non Applicable / Non Disponible**.*  
> *Pour la période 1900–1939 (GPCC), les archives historiques sont numérisées sous forme de totaux mensuels consolidés. Nous n'avons pas créé de données journalières artificielles afin de préserver l'intégrité scientifique.*  
> *À partir de 1940, la réanalyse ERA5-Land fournit un pas journalier continu, ce qui permet de calculer avec exactitude le nombre de jours de pluie (seuil normalisé OMM : précipitations $\ge 1.0\text{ mm/jour}$)."*

---

### Q4 : Que représente la courbe orange sur l'histogramme chronologique ?
> **Réponse technique :**  
> *"C'est la **Moyenne Mobile sur 10 ans** (Moyenne glissante décennale).*  
> *Elle filtre les fluctuations interannuelles chaotiques et met en évidence la tendance hydrologique séculaire, notamment la grande rupture de sécheresse des années 1970–1990 en Algérie."*

---

## 📊 2. Glossaire des Notions Scientifiques d'Ingénierie Hydraulique

| Terme / Indicateur | Définition & Valeur pour l'Algérie |
| :--- | :--- |
| **Cumul Annuel ($P_{ann}$) en mm** | Hauteur totale d'eau précipitée au cours de l'année. |
| **Résolution Spatiale 0.1° (~9 km)** | Maille de calcul d'ERA5-Land offrant une précision locale adaptée aux bassins versants. |
| **Normale Climatologique 1961–1990** | Normale séculaire historique de référence de l'OMM. |
| **Normale Climatologique 1991–2020** | Normale contemporaine reflétant l'accélération du réchauffement climatique. |
| **Anomalie Pluviométrique (%)** | Écart relatif à la normale : $\text{Anomalie} = \frac{P - P_{norm}}{P_{norm}} \times 100$. |
| **Pente de Tendance Décennale** | Taux d'évolution des précipitations par décennie ($\text{mm/décennie}$). |
| **Étage Bioclimatique d'Emberger** | Quotient pluviothermique d'Emberger ($Q_2$), reliant précipitations et températures extrêmes ($M, m$). |

---

## 🔐 3. Aide-Mémoire des Accès
- **Site Cloud :** `https://hydro-replay-algerie-1.onrender.com`
- **Serveur Local :** `http://127.0.0.1:8000`
- **Code secret d'entrée :** `2005`
- **Votre Titre :** `Ingénieure d'État en Hydraulique`
