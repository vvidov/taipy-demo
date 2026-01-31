import csv
import random
from datetime import datetime, timedelta

# Vorarlberg cities and postal codes
vorarlberg_cities = [
    ("Bregenz", 6900),
    ("Dornbirn", 6850),
    ("Feldkirch", 6800),
    ("Bludenz", 6700),
    ("Hohenems", 6845),
    ("Lustenau", 6890),
    ("Rankweil", 6830),
    ("Hard", 6971),
    ("Götzis", 6840),
    ("Altach", 6844),
    ("Frastanz", 6820),
    ("Schruns", 6780),
    ("Egg", 6863),
    ("Nenzing", 6710),
    ("Höchst", 6973),
    ("Lauterach", 6923),
    ("Wolfurt", 6922),
    ("Vandans", 6773),
    ("Bürs", 6706),
    ("Bürserberg", 6707),
    ("Mittelberg", 6993),
    ("Gaschurn", 6793),
    ("Tschagguns", 6774),
    ("Bezau", 6870),
    ("Andelsbuch", 6866),
    ("Sulz", 6832),
    ("Koblach", 6842),
    ("Satteins", 6822),
    ("Gais", 6861)
]

# Sample data for other fields
ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]
segments = ["Consumer", "Corporate", "Home Office"]
product_categories = [
    ("Furniture", "Bookcases", "Vorarlberg Oak Bookcase"),
    ("Furniture", "Chairs", "Alpine Comfort Chair"),
    ("Office Supplies", "Labels", "Austrian Address Labels"),
    ("Office Supplies", "Storage", "Vorarlberg Storage Box"),
    ("Technology", "Phones", "AlpenPhone X1"),
    ("Technology", "Laptops", "MontafonBook Pro"),
    ("Technology", "Accessories", "Bregenzer Mouse"),
    ("Technology", "Tablets", "Bodensee Tab"),
    ("Office Supplies", "Binders", "BinderPro 2026"),
    ("Office Supplies", "Paper", "Vorarlberg Copy Paper"),
    ("Furniture", "Tables", "Lake Constance Table"),
    ("Office Supplies", "Art", "Montafon Art Set"),
    ("Office Supplies", "Appliances", "Vorarlberg Desk Lamp")
]

customer_names = [
    "Anna Müller", "Lukas Hofer", "Sophie Gruber", "Maximilian Bauer", "Laura Huber",
    "Jonas Mayer", "Lea Winkler", "Paul Steiner", "Mia Fuchs", "Felix Berger"
]

regions = ["Vorarlberg"]

num_rows = 10000  # Change as needed

with open("data/data_vorarlberg.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "Row ID", "Order ID", "Order Date", "Ship Date", "Ship Mode", "Customer ID", "Customer Name",
        "Segment", "Country", "City", "State", "Postal Code", "Region", "Product ID", "Category",
        "Sub-Category", "Product Name", "Sales"
    ])
    for row_id in range(1, num_rows + 1):
        order_id = f"AT-{random.randint(2015,2025)}-{random.randint(100000,999999)}"
        order_date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365))
        ship_date = order_date + timedelta(days=random.randint(1, 7))
        ship_mode = random.choice(ship_modes)
        cust_idx = random.randint(0, len(customer_names)-1)
        customer_id = f"AT-{10000+cust_idx}"
        customer_name = customer_names[cust_idx]
        segment = random.choice(segments)
        country = "Austria"
        city, postal_code = random.choice(vorarlberg_cities)
        state = "Vorarlberg"
        region = "Vorarlberg"
        prod_cat, sub_cat, prod_name = random.choice(product_categories)
        product_id = f"{prod_cat[:3].upper()}-{sub_cat[:2].upper()}-{random.randint(10000000,99999999)}"
        sales = round(random.uniform(10, 2000), 2)
        writer.writerow([
            row_id, order_id, order_date.strftime("%d/%m/%Y"), ship_date.strftime("%d/%m/%Y"), ship_mode,
            customer_id, customer_name, segment, country, city, state, postal_code, region, product_id,
            prod_cat, sub_cat, prod_name, sales
        ])
