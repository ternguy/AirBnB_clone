#!/usr/bin/python3
"""
Sub_class City of class BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ the city name and id """

    state_id = ""
    name = ""
