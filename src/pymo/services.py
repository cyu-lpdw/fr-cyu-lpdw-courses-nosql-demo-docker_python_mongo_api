#!/usr/bin/env python3

"""
"""
from motor.motor_asyncio import AsyncIOMotorCollection

from pymo.models import User


class UsersService(object):

    def __init__(self, collection: AsyncIOMotorCollection):
        """
        Create a new instance of {UsersService}.

        :param conn: The database connection.
        """
        self.collection: AsyncIOMotorCollection = collection
        print(type(collection))

    async def create(self, user: User):
        """
        Create a new user.
        """
        return await self.collection.insert_one(user.dict())
