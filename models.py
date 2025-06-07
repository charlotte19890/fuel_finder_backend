from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Station(Base):
    __tablename__ = "stations"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    opening_hours = Column(String)
    services = Column(String)
    fuel_types = Column(String)
    image_url = Column(String)

    prices = relationship("FuelPrice", back_populates="station")

class FuelPrice(Base):
    __tablename__ = "fuel_prices"

    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(String, ForeignKey("stations.id"))
    fuel_type = Column(String)
    price = Column(Float)

    station = relationship("Station", back_populates="prices")