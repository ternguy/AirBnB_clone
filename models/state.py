#!/usr/bin/python3
<<<<<<< HEAD

"""this module creates a user class"""

from models.base_model import BaseModel


class State(BaseModel):
    """class for managing state objects"""
=======
"""
The sub_class of basemodel
"""
from models.base_model import BaseModel

class State(BaseModel):
    """ The state name """
>>>>>>> a956671c71f8783740e5109d207df2d71b62226a

    name = ""
