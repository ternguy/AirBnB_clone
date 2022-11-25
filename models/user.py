#!/usr/bin/python3
<<<<<<< HEAD
"""this model create a user class"""
from models.base_model import BaseModels


class User(BaseModel):
    """ class for managing user objects"""
=======
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
>>>>>>> a956671c71f8783740e5109d207df2d71b62226a

    email = ""
    password = ""
    first_name = ""
    last_name = ""
