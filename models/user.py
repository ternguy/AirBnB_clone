#!/usr/bin/python3
"""this model create a user class"""
from models.base_model import BaseModels


class User(BaseModel):
    """ class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
