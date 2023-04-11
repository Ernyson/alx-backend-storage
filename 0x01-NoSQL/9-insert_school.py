#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserting  new document in a collection based on kwargs
    """
    id_col = mongo_collection.insert_one(kwargs)
    return id_col.inserted_id
