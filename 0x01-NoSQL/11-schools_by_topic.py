#!/usr/bin/env python3
""" a python module to return list of sch
"""


def schools_by_topic(mongo_collection, topic):
    """a function that return the list of schools
    """
    return mongo_collection.find({"topics": topic})
