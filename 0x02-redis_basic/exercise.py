#!/usr/bin/env python3
"""This module contains functions and classes for working with Redis."""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times methods of the Cache class are called.

    Parameters:
    method (Callable): The method to be decorated.

    Returns:
    Callable: The wrapped method with count functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get the data from Redis by key and convert it using the provided
        function.

        Parameters:
        key (str): The key to retrieve the data from Redis.
        fn (Optional[Callable]): A function to convert the data back to the
        desired format.

        Returns:
        Union[str, bytes, int, float]: The data retrieved from Redis, converted
        if a function is provided.
        """
        value = self._redis.get(name=key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Get the data from Redis by key and convert it to a string.

        Parameters:
        key (str): The key to retrieve the data from Redis.

        Returns:
        str: The data retrieved from Redis, converted to a string.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Get the data from Redis by key and convert it to an integer.

        Parameters:
        key (str): The key to retrieve the data from Redis.

        Returns:
        int: The data retrieved from Redis, converted to an integer.
        """
        return self.get(key, fn=int)
