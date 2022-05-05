#!/usr/bin/env python3

"""
"""

import pytest
from mongomock_motor import AsyncMongoMockClient

from cyu.lpdw.pymo.services import UsersService


users_coll = None 
""" Database user collection. """

users_service = None
""" Users logic service. """

@pytest.fixture()
def resource(request):
    print("setup")
    conn = AsyncMongoMockClient()['tests']
    users_coll = conn.get("users")
    users_service = UsersService(conn)
    def teardown():
        print("teardown")
    request.addfinalizer(teardown)
    
    return "resource"

class ServicesTestClass:

  
  async def test_create():
    """ Unit test: create a new user.
    """
    assert await collection.find({}).to_list(None) == []
    result = await collection.insert_one({'a': 1})
    assert result.inserted_id
    assert len(await collection.find({}).to_list(None)) == 1

