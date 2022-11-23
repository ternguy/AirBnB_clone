#!/usr/bin/python3
from datatime import datetime
from uuid import uuid4
import models

"""
The base models in constructed here
"""

class BaseModel():
    """ Make a parrent class the the AirBnB clone
    Methos:
        __str__: the string method
        __init__: The initialization method
        __repr__: The copy of str method
        __save__: the save method
        to_dict__: The dictionary setting method
    """

    def __init__(self, *agrs, **kwargs):
        """ Initialize the method
        Args:
            *args: the length argument
            **kwargs: The dictionary elements
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.item():
                if "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"], date_format)

                elif "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"], date_format)

                elif '__class__' == key:
                    pass
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Print the class_name, id and dict """
        return ("[{}] ({}) {}".format(self.__class__.name,
                                        self.id, self.__dict__))

    def __repr__(self):
        """ Return the copy of the __str__ """
        return (self.__str__())

    def __save__(self):
        """ Save to update the puplic instance to the currrent time """
        self.updated_at = datetime.now()
        models.storate.save()

    def to_dict(self):
        """ Return a dictionary containing all keys/values of __dict__ """
        dic = self.__dict__.copy()
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        dic['__class__'] = self.__class__.name__

        return (dic)
