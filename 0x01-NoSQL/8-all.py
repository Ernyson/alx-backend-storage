#!/usr/bin/env python3
"""
function that list all documents a in Python module
"""


def list_all(mongo_collection):
    """ Now lists all documents in the collection """
    return mongo_collection.find()
