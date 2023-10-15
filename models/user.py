#!/usr/bin/env python3
"""Inheritance for BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Explains the characteristics of the User.

    Attributes:
        email: string - null string
        password: string - empty
        first_name: string - empty
        last_name: string - empty
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
