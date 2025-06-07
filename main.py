from fastapi import FastAPI
from database import create_tables

app = FastAPI()

create_tables()  # This will create tables when app starts

from fastapi import FastAPI, HTTPException

# Fuel prices per station
fuel_prices = {
    "go001": {
        "Unleaded 93": 21.50,
        "Unleaded 95": 22.30,
        "Diesel": 20.80
    },
    "go002": {
        "Unleaded 93": 21.60,
        "Diesel": 20.75
    },
    "go003": {
        "Unleaded 95": 22.40,
        "Diesel": 20.90
    }
}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Global Oil Garage Fuel Finder Backend is running 🚀"}

# Stations endpoint with full details
@app.get("/stations")
def get_stations():
    return [
        {
            "id": "go001",
            "name": "Global Oil Garage Sandton",
            "address": "123 Main St, Sandton, Johannesburg",
            "phone": "+27 11 123 4567",
            "location": {"lat": -26.107, "lng": 28.056},
            "opening_hours": "06:00 - 22:00",
            "services": ["Car Wash", "ATM", "Cafe", "Restrooms", "Wi-Fi", "Convenience Store"],
            "fuel_types": ["Unleaded 93", "Unleaded 95", "Diesel"],
            "image_url": "https://example.com/images/station_go001.jpg"
        },
        {
            "id": "go002",
            "name": "Global Oil Garage Rosebank",
            "address": "45 Rosebank Rd, Rosebank, Johannesburg",
            "phone": "+27 11 765 4321",
            "location": {"lat": -26.142, "lng": 28.031},
            "opening_hours": "05:30 - 23:00",
            "services": ["ATM", "Cafe", "Restrooms", "Convenience Store"],
            "fuel_types": ["Unleaded 93", "Diesel"],
            "image_url": "https://example.com/images/station_go002.jpg"
        },
        {
            "id": "go003",
            "name": "Global Oil Garage Johannesburg Central",
            "address": "78 Market St, Johannesburg Central",
            "phone": "+27 11 998 8776",
            "location": {"lat": -26.204, "lng": 28.047},
            "opening_hours": "24/7",
            "services": ["Car Wash", "Restrooms", "Wi-Fi"],
            "fuel_types": ["Unleaded 95", "Diesel"],
            "image_url": "https://example.com/images/station_go003.jpg"
        }
    ]

# Price endpoint with station ID param
@app.get("/prices/{station_id}")
def get_prices(station_id: str):
    prices = fuel_prices.get(station_id)
    if prices is None:
        raise HTTPException(status_code=404, detail="Station not found")
    return {"station_id": station_id, "prices": prices}