#!/usr/bin/env python3

"""
"""

class UsersService(object):

    def __init__(self, conn):
       """ 
       Create a new instance of {UsersService}.

       :param conn: The database connection.
       """


    await def create(self, user: User):
       """
       Create a new user.
       """
       return await self.collection.insert_one(user.dict())


