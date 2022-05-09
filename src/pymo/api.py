#!/usr/bin/env python3

"""
@see: https://fastapi.tiangolo.com/tutorial/first-steps/ 
"""
import logging

from fastapi import FastAPI

from pymo.db import DatabaseConnectionHelper
from pymo.models import User
from pymo.services import UsersService


LOGGER = logging.getLogger(__name__)
""" The module logger. """


# Create the FastAPI application.
app = FastAPI()

db_conn_helper = DatabaseConnectionHelper()

# Start or stop database connection on application related events.
app.add_event_handler("startup", db_conn_helper.connect_db)
app.add_event_handler("shutdown", db_conn_helper.close_db)

# Create a new instances for each services
users_service = UsersService(db_conn_helper.engine, User)
LOGGER.info("users_service", extra={"users_service.engine": users_service.engine})


@app.post("/user")
async def create_user(user: User):
    # user = User(email="camille.martin@example.org", firstname="Camille", lastname="Martin")
    result = await users_service.create(user)
    LOGGER.info("result", extra={"result": result})
    return result
