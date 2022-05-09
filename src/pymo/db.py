#!/usr/bin/env python3
import logging

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from pymo import settings

from motor.motor_asyncio import AsyncIOMotorClient


LOGGER = logging.getLogger(__name__)


class DatabaseConnectionHelper(object):

    def __init__(self):
        self.db_client = AsyncIOMotorClient(settings.DATABASE_URI)
        self.engine = None

    async def connect_db(self):
        """Create database connection."""
        LOGGER.debug("connect_db()")
        self.engine = AIOEngine(motor_client=self.db_client, database=settings.DATABASE_NAME)

    async def close_db(self):
        """Close database connection."""
        LOGGER.debug("close_db()")
        self.db_client.close()
