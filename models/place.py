#!/usr/bin/python3
"""
Sub_class of the BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ declare some attributes selated to place """

    city_id = ""
    user_id = ""
    name = ""
    desctiption = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
