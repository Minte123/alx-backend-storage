#!/usr/bin/env python3
"""python module to access documents in a collection"""
from pymongo import MongoClient
def list_all(mongo_collection):
    """function that lists all documents in a collection"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    if (mongo_collection.find()):
        return mongo_collection.find()
    else:
        return []
