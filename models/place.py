#!/usr/bin/python3
"""
Sub_class
"""

class Place(BaseModel):
    """ Inform the place (location) """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_gues = 0
    price_by_night = 0
    longitude = 0.0
    latitude = 0
    amenity_ids = []
