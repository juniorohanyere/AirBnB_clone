#!/usr/bin/python3
""" This module contains  Amenity class (Child-class to BaseModel) """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Implement the Amenity class.

    Args:
        name(str): name of the amenity.
    """
    name = ""
