#!/usr/bin/python3
"""Amenity class module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Initialization of the Amenity class.

    Args:
        name(str): name of the amenity.
    """
    name = ""
