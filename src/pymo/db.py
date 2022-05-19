#!/usr/bin/env python3
import logging

import motor
from beanie import init_beanie

from pymo import settings

from motor.motor_asyncio import AsyncIOMotorClient

from pymo.models import User
from pymo.settings import Settings

LOGGER = logging.getLogger(__name__)



class DatabaseConnection(object):

    LOG = LOGGER.getChild("DatabaseConnection")
    """ The class logger. """

    instance = None
    conn = None
    db = None
    settings = Settings()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    async def open(self) -> motor.motor_asyncio.AsyncIOMotorClient:
        """ Open a database connection.

        :param app: The FastAPI application.
        :return: Function to call at application startup.
        """
        self.conn = motor.motor_asyncio.AsyncIOMotorClient(self.settings.DATABASE_URI)
        self.db = self.conn[self.settings.DATABASE_NAME]
        await init_beanie(database=self.db, document_models=[User])

    async def close(self):
        """ Close the database connection.

        :param app: The FastAPI application.
        :return: Function to run at application shutdown.
        """
        self.conn.close()
