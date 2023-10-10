#!/usr/bin/env python3
"""module for the base model for all other modules/models
"""

import uuid
from datetime import datetime


class BaseModel:
    """class that defines all common attributes/methods for all
    other classes
    """

    def __init__(self):
        """instantiation class
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>
        """

        dictionary = str({a: b for (a, b) in self.__dict__.items() if (not b)
                         is False})
        return ("[" + self.__class__.__name__ + "] (" + self.id + ") " +
                dictionary)
