from sqlalchemy.orm import Session
from database import SessionLocal
from models import Station, FuelPrice

def seed():
    db: Session = SessionLocal()

    # Clear old data
    db.query(FuelPrice).delete()
    db.query(Station).delete()

    # Sample stations
    stations = [
        Station(
            id="go001",
            name="Global Oil Garage Sandton",
            address="123 Main St, Sandton, Johannesburg",
            phone="+27 11 123 4567",
            lat=-26.107,
            lng=28.056,
            opening_hours="06:00 - 22:00",
            services="Car Wash,ATM,Cafe,Restrooms,Wi-Fi,Convenience Store",
            fuel_types="Unleaded 93,Unleaded 95,Diesel",
            image_url="https://example.com/images/station_go001.jpg"
        ),
        Station(
            id="go002",
            name="Global Oil Garage Rosebank",
            address="45 Rosebank Rd, Rosebank, Johannesburg",
            phone="+27 11 765 4321",
            lat=-26.142,
            lng=28.031,
            opening_hours="05:30 - 23:00",
            services="ATM,Cafe,Restrooms,Convenience Store",
            fuel_types="Unleaded 93,Diesel",
            image_url="https://example.com/images/station_go002.jpg"
        ),
        Station(
            id="go003",
            name="Global Oil Garage Johannesburg Central",
            address="78 Market St, Johannesburg Central",
            phone="+27 11 998 8776",
            lat=-26.204,
            lng=28.047,
            opening_hours="24/7",
            services="Car Wash,Restrooms,Wi-Fi",
            fuel_types="Unleaded 95,Diesel",
            image_url="https://example.com/images/station_go003.jpg"
        )
    ]

    db.add_all(stations)

    # Sample fuel prices
    prices = [
        FuelPrice(station_id="go001", fuel_type="Unleaded 93", price=21.50),
        FuelPrice(station_id="go001", fuel_type="Unleaded 95", price=22.30),
        FuelPrice(station_id="go001", fuel_type="Diesel", price=20.80),

        FuelPrice(station_id="go002", fuel_type="Unleaded 93", price=21.60),
        FuelPrice(station_id="go002", fuel_type="Diesel", price=20.75),

        FuelPrice(station_id="go003", fuel_type="Unleaded 95", price=22.40),
        FuelPrice(station_id="go003", fuel_type="Diesel", price=20.90)
    ]

    db.add_all(prices)
    db.commit()
    db.close()
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed()