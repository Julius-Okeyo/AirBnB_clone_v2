import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class PlaceAmenity(BaseModel, Base):
    '''
    Defines a join table for handling many to many
    relationship between Place and Amenities.
    '''
    __tablename__ = "place_amenities"
    amenity_id = Column(String, ForeignKey("amenities.id"))
    place_id = Column(String, ForeignKey("places.id"))
