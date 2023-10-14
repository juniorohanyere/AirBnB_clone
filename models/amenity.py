#!/usr/bin/python3
""" Module of  Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Deployment of the Amenity class.

    Args:
        name(str): name of the amenity.
    """
    name = ""
