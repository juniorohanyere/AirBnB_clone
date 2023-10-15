#!/usr/bin/env python3
"""BaseModel for city class inheritance"""
from models.base_model import BaseModel


class City(BaseModel):
    """Summarize the design plan for the City.

    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
