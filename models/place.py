#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import environ


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if environ["HBNB_TYPE_STORAGE"] == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")

    else:
        @property
        def reviews(self):
            """ getter method for reviews"""
            reviews_list = []
            reviews = models.storage.all(Reviews)
            for review in reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
