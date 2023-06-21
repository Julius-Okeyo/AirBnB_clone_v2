#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """
    Defines class Amenity with attributes name and place
    """
    from models.place import Place
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    places = relationship("Place", secondary=place_amenities_assoc, viewonly=False, back_populates="amenities")
