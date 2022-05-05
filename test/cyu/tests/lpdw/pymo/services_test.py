#!/usr/bin/env python3

"""
"""
import pytest
from mongomock_motor import AsyncMongoMockClient

@pytest.fixture()
def resource(request):
    print("setup")

    def teardown():
        print("teardown")
    request.addfinalizer(teardown)
    
    return "resource"

class TestClass:

  
  async def test_mock_client():
    collection = AsyncMongoMockClient()['tests']['test-1']
    assert await collection.find({}).to_list(None) == []
    result = await collection.insert_one({'a': 1})
    assert result.inserted_id
    assert len(await collection.find({}).to_list(None)) == 1

