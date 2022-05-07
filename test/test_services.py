#!/usr/bin/env python3

"""

:see: https://dev.to/jphutchins/update-python-unittest-with-asyncio-tests-for-aiohttp-and-more-31aj
"""
import asyncio
import unittest
import sys
from os.path import join, dirname, abspath
from unittest import async_case


sys.path.append(abspath(join(dirname(__file__), "..", "src")))
print(sys.path)

from pymo.models import User
from pymo.services import UsersService
from utils import async_test


from mongomock_motor import AsyncMongoMockClient

class ServicesTestClass(unittest.TestCase):

    def setUp(self):
        """

        :return:
        """
        self.users_collection = AsyncMongoMockClient()['tests']["users"]
        self.users_service = UsersService(self.users_collection)

    @classmethod
    def setUpClass(cls):
        # you probably have some existing code above here
        cls.loop = ServicesTestClass._create_event_loop()

    @classmethod
    def _create_event_loop(cls):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop

    # @async_test
    # async def test_create(self):
    #     """ Unit test: create a new user.
    #     """
    #     data_test = {"email": "camille.martin@example.org", "firstname": "Camille", "lastname": "Martin"}
    #     assert await self.users_collection.find({}).to_list(None) == []
    #     result = await self.users_collection.insert_one(data_test)
    #     assert result.inserted_id
    #     assert len(await self.users_collection.find({"email": "camille.martin@example.org"}).to_list(None)) == 1

    @async_test
    async def test_create(self):
        user = User(email="camille.martin@example.org", firstname="Camille", lastname="Martin")
        result = await self.users_service.create(user)
        assert result.inserted_id
        assert len(await self.users_collection.find({"email": "camille.martin@example.org"}).to_list(None)) == 1

if __name__ == "__main__":
    unittest.main()
