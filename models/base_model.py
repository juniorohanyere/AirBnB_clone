#!/usr/bin/env python3
"""Basemodule for all other modules"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Common attributes class definitions"""

    def __init__(self, *args, **kwargs):
        """instance initializing class

        Args:
            args (list): non-keyworded variable length list of arguments
            kwargs (list): keyworded variable length list of arguments
        """

        if kwargs:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'

            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(kwargs[key], fmt)
                if key != '__class__':
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>
        """

        dictionary = str({a: b for (a, b) in self.__dict__.items() if (not b)
                         is False})
        return ("[" + self.__class__.__name__ + "] (" + self.id + ") " +
                dictionary)

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance
        """

        fmt = '%Y-%m-%dT%H:%M:%S.%f'
        dictionary = {}

        for key, val in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dictionary[key] = val.strftime('%Y-%m-%dT%H:%M:%S.%f')
            elif val:
                dictionary[key] = val

        dictionary['__class__'] = self.__class__.__name__

        return (dictionary)
