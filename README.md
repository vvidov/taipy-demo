
# Taipy Demo: Vorarlberg & US Sales Dashboard

This project is based on the [Avaiga/taipy-course-gui](https://github.com/Avaiga/taipy-course-gui) repository, with customizations for Vorarlberg, Austria and additional features.

This project is a demo dashboard built with Taipy GUI for visualizing and filtering sales data for both the US and Vorarlberg, Austria. It features interactive charts, maps, and filters for categories, sub-categories, and dates.

## Features
- Interactive dashboard with menu navigation
- US sales by state (bar chart and map)
- Vorarlberg sales by city (bar chart and map)
- Filtering by product category, sub-category, and date range
- Synthetic data generation for Vorarlberg
- Modular code structure (pages, maps, data)

## Project Structure
```
├── data/                      # CSV data files
│   ├── data.csv               # US sales data
│   └── data_vorarlberg.csv    # Vorarlberg sales data (generated)
├── images/                    # Icon and map images (SVG/PNG)
├── maps/                      # Map rendering modules
│   ├── us_map.py
│   └── vorarlberg_map.py
├── pages/                     # Taipy GUI page modules
│   ├── sales_page.py
│   ├── sales_vorarlberg_page.py
│   └── max_page.py
├── generate_vorarlberg_data.py# Script to generate Vorarlberg data
├── main.py                    # Main app entry point
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Setup & Usage
1. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
2. **Generate Vorarlberg data** (if needed)
   ```sh
   python generate_vorarlberg_data.py
   ```
3. **Run the dashboard**
   ```sh
   python main.py
   ```

## Customization
- To add more cities, categories, or sub-categories, edit `generate_vorarlberg_data.py`.
- To change icons, replace SVG/PNG files in the `images/` folder.
- To add new pages, create a new file in `pages/` and register it in `main.py`.

## Requirements
- Python 3.8+
- Taipy GUI
- pandas
- plotly

## License
MIT License

---
Demo project for data visualization and dashboarding with Taipy GUI.
