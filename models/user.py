#!/usr/bin/python3
"""
sub_class model
"""

import json
from models.base_model import BaseModel

class User(BaseModel):
    """ The user class
    Args:
        email(string): the empty string
        password(string): empty string
        first_name(string): empty string
        last_name(string): empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
