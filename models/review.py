#!/usr/bin/env python3
"""Review Class inheritance basemodel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Summarizes the design plan of the Review.

    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
