#!/usr/bin/env python3

"""

:see: https://dev.to/jphutchins/update-python-unittest-with-asyncio-tests-for-aiohttp-and-more-31aj
"""
import asyncio
import logging
import unittest
import sys
from os.path import join, dirname, abspath
from unittest import async_case, mock

import mongomock
import pymongo
from odmantic import AIOEngine

from pymo.utils import setup_logging

sys.path.append(abspath(join(dirname(__file__), "..", "src")))
print(sys.path)

from pymo.models import User
from pymo.services import UsersService
from utils import async_test

from mongomock_motor import AsyncMongoMockClient

setup_logging()




class ServicesTestClass(unittest.TestCase):

    def setUp(self):
        """

        :return:
        """
        logging.info("Setup")

        self.engine = AIOEngine(motor_client=AsyncMongoMockClient()['test'])
        print(self.engine)

        self.model = User
        self.users_service = UsersService(self.engine, self.model)
        logging.info("client", extra={"engine": self.engine})

    @classmethod
    def setUpClass(cls):
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
    #     assert await self.model.find({}).to_list(None) == []
    #     result = await self.model.insert_one(data_test)
    #     assert result.inserted_id
    #     assert len(await self.model.find({"email": "camille.martin@example.org"}).to_list(None)) == 1

    @async_test
    async def test_create(self):
        user = User(email="camille.martin@example.org", firstname="Camille", lastname="Martin")
        result = await self.users_service.create(user)
        # assert len(await self.engine.find(self.model, getattr(self.model, "email")) == "camille.martin@example.org") == 1
        # assert len(await native_db_collection.find({"email": "camille.martin@example.org"}).to_list(None)) == 1
        print("result", result)
        # assert result.email == "camille.martin@example.org", "firstname"
        # assert result.firstname == "Camille"
        # assert result.lastname == "Martin"


if __name__ == "__main__":
    unittest.main()
