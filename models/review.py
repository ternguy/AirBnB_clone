#!/usr/bin/python3
"""
Sub_class
"""
from models.base_model import BaseModel
class Review(BaseModel):
    """ The reviews information """

    place_id = ""
    user_id = ""
    text = ""
