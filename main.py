from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Station, FuelPrice

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Global Oil Fuel Finder"}

@app.get("/stations")
def get_stations(db: Session = Depends(get_db)):
    return db.query(Station).all()

@app.get("/stations/{station_id}")
def get_station(station_id: str, db: Session = Depends(get_db)):
    return db.query(Station).filter(Station.id == station_id).first()

@app.get("/stations/{station_id}/prices")
def get_prices_for_station(station_id: str, db: Session = Depends(get_db)):
    return db.query(FuelPrice).filter(FuelPrice.station_id == station_id).all()