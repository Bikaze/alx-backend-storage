#!/usr/bin/env python3
"""
This module provides a function to search for schools by a specific topic
in a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Parameters:
    mongo_collection: The pymongo collection object.
    topic (str): The topic searched.

    Returns:
    A list of schools that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
