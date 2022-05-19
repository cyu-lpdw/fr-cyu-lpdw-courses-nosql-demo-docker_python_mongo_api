#!/usr/bin/env python3

"""
@see: https://fastapi.tiangolo.com/tutorial/first-steps/ 
"""
import logging

from fastapi import FastAPI, Depends, APIRouter

from pymo.db import DatabaseConnection
from pymo.models import User
from pymo.services import UsersService, get_services

LOGGER = logging.getLogger(__name__)
""" The module logger. """


main_router = APIRouter()
services = Depends(get_services()).dependency

@main_router.post("/user")
async def create_user(user: User):
    """ Create a new user.

    :param user: The user object.
    """
    result = await services.users.create(user)
    LOGGER.info("result", extra={"result": result})
    return result

print("main_router", main_router)