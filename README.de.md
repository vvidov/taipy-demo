# Taipy Demo: Vorarlberg & US Sales Dashboard (Deutsch)

Dieses Projekt basiert auf dem [Avaiga/taipy-course-gui](https://github.com/Avaiga/taipy-course-gui) Repository und wurde für Vorarlberg, Österreich, sowie zusätzliche Funktionen angepasst.

## Funktionen
- Interaktives Dashboard mit Menü-Navigation
- US-Umsätze nach Bundesstaat (Balkendiagramm und Karte)
- Vorarlberger Umsätze nach Stadt (Balkendiagramm und Karte)
- Filterung nach Produktkategorie, Unterkategorie und Zeitraum
- Generierung synthetischer Daten für Vorarlberg
- Modulare Code-Struktur (pages, maps, data)

## Projektstruktur
```
├── data/                      # CSV-Datendateien
│   ├── data.csv               # US-Umsatzdaten
│   └── data_vorarlberg.csv    # Vorarlberg-Umsatzdaten (generiert)
├── images/                    # Icon- und Kartenbilder (SVG/PNG)
├── maps/                      # Module für Kartenvisualisierung
│   ├── us_map.py
│   └── vorarlberg_map.py
├── pages/                     # Taipy GUI Seitenmodule
│   ├── sales_page.py
│   ├── sales_vorarlberg_page.py
│   └── max_page.py
├── generate_vorarlberg_data.py# Skript zur Datengenerierung für Vorarlberg
├── main.py                    # Haupteinstiegspunkt der App
├── requirements.txt           # Python-Abhängigkeiten
└── README.de.md               # Diese Datei
```

## Einrichtung & Nutzung
1. **Abhängigkeiten installieren**
   ```sh
   pip install -r requirements.txt
   ```
2. **Vorarlberg-Daten generieren** (falls benötigt)
   ```sh
   python generate_vorarlberg_data.py
   ```
3. **Dashboard starten**
   ```sh
   python main.py
   ```

## Anpassung
- Um weitere Städte, Kategorien oder Unterkategorien hinzuzufügen, bearbeiten Sie `generate_vorarlberg_data.py`.
- Um Icons zu ändern, ersetzen Sie SVG/PNG-Dateien im `images/`-Ordner.
- Um neue Seiten hinzuzufügen, erstellen Sie eine neue Datei in `pages/` und registrieren Sie sie in `main.py`.

## Voraussetzungen
- Python 3.8+
- Taipy GUI
- pandas
- plotly

## Lizenz
MIT-Lizenz

---
Demo-Projekt für Datenvisualisierung und Dashboards mit Taipy GUI.
