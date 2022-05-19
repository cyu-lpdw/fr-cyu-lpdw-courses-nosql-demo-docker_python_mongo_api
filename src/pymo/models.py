#!/usr/bin/env python3

"""
Module containing models.
"""
from beanie import Document
from pydantic import Field
from pydantic.networks import EmailStr


class User(Document):
    """
    The user model.
    """

    email: EmailStr = Field(...)
    """ The e-mail address is the unique identifier of a user. """

    firstname: str = Field(...)
    """ The firstname of user. """

    lastname: str = Field(...)
    """ The lastname of user. """
