#!/usr/bin/env python3

"""
"""
from unittest import mock
from unittest.mock import AsyncMock

from motor.motor_asyncio import AsyncIOMotorCollection
from odmantic import Model
from pymongo.results import InsertOneResult

from pymo.models import User

# request_mock = AsyncMock()
# request_mock.__aenter__.return_value = request_mock
# request_mock.json.return_value = { 'hello' : 'world'}


class OdmanticEngineMock(mock.AsyncMock):
    pass

class UsersService(object):

    def __init__(self, db_engine, model: Model):
        """
        Create a new instance of {UsersService}.

        :param conn: The database connection.
        """
        self.engine = db_engine
        self.model = model
        print(type(self.model))

    async def create(self, user: User):
        """
        Create a new user.
        """
        oid: InsertOneResult = await self.engine.save(user)
        print(oid)
        o = await self.engine.find_one(self.model, getattr(self.model, "id"))
        print("type(o)", type(o))
        return o
