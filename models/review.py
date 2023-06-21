#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """
    Defines class Review
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    place_review = relationship("Place", backref="places")
