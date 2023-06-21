#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place_amenity import PlaceAmenityAssoc

class Amenity(BaseModel, Base):
    """
    Defines class Amenity with attributes name and place
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    places = relationship("Place", secondary="place_amenities_assoc", viewonly=False, backref="amenities")
