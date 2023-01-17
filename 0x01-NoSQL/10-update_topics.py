#!/usr/bin/env python3
"""pymong update documents"""
from pymongo import MongoClient
def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school document based on the name"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    query = { "name": name }
    newValues = { "$set": { "topics": topics } }
    mongo_collection.update_many(query, newValues)
