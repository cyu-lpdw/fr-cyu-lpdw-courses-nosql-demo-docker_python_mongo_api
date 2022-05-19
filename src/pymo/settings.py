#!/usr/bin/env python3

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DATABASE_URI: str = Field(env="DATABASE_URI", default="mongodb://localhost:27017/")
    DATABASE_NAME: str = Field(env='DATABASE_NAME', default="pymo")

    LOG_LEVEL: str = Field(env="LOG_LEVEL", default="DEBUG")
