#!/usr/bin/python3
'''
Defines a class that associates two other classes
'''
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class PlaceAmenityAssoc(BaseModel, Base):
    '''
    Defines a class that associates two other classes
    '''
    __tablename__ = "place_amenities_assoc"
    amenity_id = Column(String, ForeignKey("amenities.id"), primary_key=True, nullable=False)
    place_id = Column(String, ForeignKey("places.id"), primary_key=True, nullable=False)
