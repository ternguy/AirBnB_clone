#!/usr/bin/python3
"""
The sub_class of BaseModel
"""
from models.base_model import BaseModel

class City(BaseModel):
    """ City id and name """

    state_id = ""
    name = ""
