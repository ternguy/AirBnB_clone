#!/usr/bin/python3
"""
Sub_class of the Base_model mother class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Show some review attributes """

    place_id = ""
    user_id = ""
    text = ""
