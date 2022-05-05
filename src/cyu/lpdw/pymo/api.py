#!/usr/bin/env python3

"""
@see: https://fastapi.tiangolo.com/tutorial/first-steps/ 
"""


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
