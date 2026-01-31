import pandas as pd
import plotly.express as px

def generate_vorarlberg_map(data: pd.DataFrame):
    vorarlberg_coords = {
        "Bregenz": (47.5031, 9.7471),
        "Dornbirn": (47.4125, 9.7417),
        "Feldkirch": (47.2371, 9.6009),
        "Bludenz": (47.1569, 9.8167),
        "Hohenems": (47.3667, 9.6833),
        "Lustenau": (47.4269, 9.6561),
        "Rankweil": (47.2833, 9.6500),
        "Hard": (47.4833, 9.6833),
        "Götzis": (47.3333, 9.6333),
        "Altach": (47.3500, 9.6500),
        "Frastanz": (47.2167, 9.6167),
        "Schruns": (47.0781, 9.9211),
        "Egg": (47.4000, 9.9000),
        "Nenzing": (47.1833, 9.6833),
        "Höchst": (47.4667, 9.6333),
        "Lauterach": (47.4833, 9.7333),
        "Wolfurt": (47.4667, 9.7333),
        "Vandans": (47.0833, 9.8667),
        "Bürs": (47.1833, 9.8167),
        "Bürserberg": (47.1667, 9.8167),
        "Mittelberg": (47.3500, 10.1500),
        "Gaschurn": (46.9833, 10.0333),
        "Tschagguns": (47.0833, 9.9000),
        "Bezau": (47.3833, 9.9833),
        "Andelsbuch": (47.4000, 9.9000),
        "Sulz": (47.3167, 9.6333),
        "Koblach": (47.3167, 9.6000),
        "Satteins": (47.2333, 9.6667),
        "Gais": (47.3667, 9.9000)
    }
    city_sales = data.groupby("City")["Sales"].sum().reset_index()
    city_sales["lat"] = city_sales["City"].map(lambda c: vorarlberg_coords.get(c, (None, None))[0])
    city_sales["lon"] = city_sales["City"].map(lambda c: vorarlberg_coords.get(c, (None, None))[1])
    city_sales = city_sales.dropna(subset=["lat", "lon"])
    fig = px.scatter_mapbox(
        city_sales,
        lat="lat",
        lon="lon",
        size="Sales",
        color="Sales",
        hover_name="City",
        hover_data={"Sales":":.2f", "lat":False, "lon":False},
        range_color=(city_sales["Sales"].min()/2, city_sales["Sales"].max()),
        color_continuous_scale="Blues",
        size_max=30,
        zoom=8,
        mapbox_style="carto-positron",
        title="Sales by City in Vorarlberg, Austria"
    )
    fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
    return fig
