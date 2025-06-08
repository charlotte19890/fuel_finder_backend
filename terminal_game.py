import json

# Load the stations
with open("global_oil_stations.json", "r") as f:
    stations = json.load(f)

# Step 1: Get all provinces
provinces = sorted(set(station["province"] for station in stations))

# Step 2: Choose province
print("Welcome to the Global Oil Station Finder 🚗⛽")
print("Choose your province:")

for i, province in enumerate(provinces, start=1):
    print(f"{i}. {province}")

province_choice = int(input("Enter the number of your province: ")) - 1
selected_province = provinces[province_choice]

# Step 3: Choose station
area_stations = [s for s in stations if s["province"] == selected_province]
print(f"\nStations in {selected_province}:")

for i, station in enumerate(area_stations, start=1):
    print(f"{i}. {station['name']} - {station['area']}")

station_choice = int(input("Enter the number of the station you want to go to: ")) - 1
selected_station = area_stations[station_choice]

# Step 4: Display coordinates and details
print("\n📍 Station Details:")
print(f"Name: {selected_station['name']}")
print(f"Address: {selected_station['address']}")
print(f"Phone: {selected_station['phone']}")
print(f"GPS: ({selected_station['lat']}, {selected_station['lng']})")
print("🛣️ Ready to Go!")