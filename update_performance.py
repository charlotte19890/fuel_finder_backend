import json

# Load the station performance data Sharlot provided
performance_raw = [
    # Format: (station name keyword, area, province, performance level)
    ("Westenburg", "Polokwane", "Limpopo", "good"),
    ("Kgebetli", "Polokwane", "Limpopo", "poor"),
    ("Nape", "Polokwane", "Limpopo", "normal"),
    ("Mawasha", "Polokwane", "Limpopo", "normal"),
    ("Total auto", "Polokwane", "Limpopo", "poor"),
    ("Dikgale", "Polokwane", "Limpopo", "normal"),
    ("Sebayeng", "Polokwane", "Limpopo", "normal"),
    ("Mogwadi", "Bochum", "Limpopo", "good"),
    ("Senwabarwana", "Bochum", "Limpopo", "normal"),
    ("Ramanwa", "Venda", "Limpopo", "normal"),
    ("Tanani", "Venda", "Limpopo", "normal"),
    ("Malvis", "Venda", "Limpopo", "normal"),
    ("Hevilesh", "Venda", "Limpopo", "poor"),
    ("Masia", "Venda", "Limpopo", "good"),
    ("Crossroads", "Venda", "Limpopo", "poor"),
    ("Mackauckau", "Venda", "Limpopo", "poor"),
    ("Mangondi", "Venda", "Limpopo", "normal"),
    ("Tshisahulu", "Venda", "Limpopo", "good"),
    ("Tshakhuma", "Venda", "Limpopo", "normal"),
    ("Lemba", "Venda", "Limpopo", "normal"),
    ("Khavhade", "Venda", "Limpopo", "normal"),
    ("Mnm", "Venda", "Limpopo", "poor"),
    ("Matavhela", "Venda", "Limpopo", "poor"),
    ("Matshidza", "Venda", "Limpopo", "good"),
    ("Mavhunga", "Venda", "Limpopo", "poor"),
    ("Dzanani", "Venda", "Limpopo", "good"),
    ("Gerry", "Tzaneen", "Limpopo", "normal"),
    ("Moleketla", "Tzaneen", "Limpopo", "poor"),
    ("Petol fuel", "Tzaneen", "Limpopo", "poor"),
    ("Madumeleng", "Tzaneen", "Limpopo", "normal"),
    ("Mokwakwaila", "Tzaneen", "Limpopo", "poor"),
    ("Khujwane", "Tzaneen", "Limpopo", "normal"),
    ("Poo ke nna", "Tzaneen", "Limpopo", "good"),
    ("The oaks", "Tzaneen", "Limpopo", "poor"),
    ("Crossroads", "Venda", "Limpopo", "poor"),  # already repeated
]

# Sample station to apply changes to (you sent Crossroads station earlier)
station_sample = {
    "id": "go015",
    "name": "Global Oil Garage Crossroads",
    "province": "Limpopo",
    "area": "Venda",
    "address": "Crossroads, Venda, Limpopo, South Africa",
    "phone": "015 2988168",
    "lat": -23.949939,
    "lng": 28.926392,
    "opening_hours": "06:00 - 22:00",
    "services": "ATM,Cafe,Restrooms,Convenience Store",
    "fuel_prices": [
        {"fuel_type": "Unleaded 93", "price": 21.6},
        {"fuel_type": "Unleaded 95", "price": 21.6}
    ]
}

# Try to match and add performance
for name_kw, area, province, performance in performance_raw:
    if (name_kw.lower() in station_sample["name"].lower() and
        area.lower() == station_sample["area"].lower() and
        province.lower() == station_sample["province"].lower()):
        station_sample["performance"] = performance
        break

# Save updated station
output_path = "global_oil_station_sample_updated.json"
with open(output_path, "w") as f:
    json.dump(station_sample, f, indent=2)

output_path