#!/usr/bin/env python3
"""This module contains functions and classes for working with Redis."""

import redis
import uuid
from typing import Union


class Cache:
    """
    A class that represents a cache using Redis.

    Methods:
    - __init__: Initialize the Cache class.
    - store: Store the input data in Redis using a random key.
    """

    def __init__(self):
        """Initialize the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key.

        Parameters:
        data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
        str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key
