#!/usr/bin/env python3

"""
"""
import logging
from unittest import mock

from beanie import Document
from dotmap import DotMap

from pymo.db import DatabaseConnection
from pymo.models import User

LOGGER = logging.getLogger(__name__)


class BaseService(object):

    def __init__(self, db, model: Document):
        self.db, self.model = db, model


class UsersService(BaseService):

    LOG = LOGGER.getChild("UsersService")
    """ The class logger. """

    def __init__(self, db_engine, model: User):
        """
        Create a new instance of {UsersService}.

        :param conn: The database connection.
        """
        self.engine = db_engine
        self.model = model
        print(type(self.model))

    def __init__(self, db):
        """ Create a new instance of MetricsService.
        """
        self.LOG.debug("__init__(db)", extra={"db": db})
        super().__init__(db, User)

    async def create(self, metric: User):
        self.LOG.info("create")
        res = await metric.create()
        found = await self.model.find_one(getattr(self.model, "id") == res.id)
        # if found is None:
        #    raise UserCreateErrorAPI
        return found


def get_services():
    LOGGER.debug("get_services()")
    db = DatabaseConnection().db
    users_service = UsersService(db)
    return DotMap(users=users_service)