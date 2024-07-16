#!/usr/bin/env python3
"""
This module provides a function to insert a new document into a MongoDB
collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs.

    Parameters:
    mongo_collection: The collection to insert the document into.
    **kwargs: Arbitrary keyword arguments that define the document.

    Returns:
    The new document's ID.
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id


if __name__ == "__main__":
    pass
