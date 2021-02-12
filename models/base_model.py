#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes

"""
from datetime import datetime
import uuid


class BaseModel():
    """Base class for the console

    """
    def __init__(self, *args, **kwargs):
        """instance initiation method

        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key is not '__class__':
                    if key is "created_at" or key is "updated_at":
                        setattr(self, key, datetime.
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the print() and str() representation

        """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """saves the instance and updated the updated_at time

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """return the dictionary of the instance

        """
        inst_dict = self.__dict__
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict
