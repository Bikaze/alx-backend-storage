#!/usr/bin/env python3
"""This module web.py contains a function that fetches the HTML content
of a URL, with caching and access counting."""

import requests
import redis
from functools import wraps

# Assuming Redis is running on localhost with the default port
r = redis.Redis()


def cache_response(func):
    @wraps(func)
    def wrapper(url):
        # Construct Redis keys for count and cache
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        # Increment the access count for the URL
        r.incr(count_key)

        # Check if the URL's content is already cached
        cached_content = r.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # If not cached, call the original function to fetch the content
        content = func(url)

        # Cache the fetched content with an expiration time of 10 seconds
        r.setex(cache_key, 10, content)
        return content
    return wrapper


@cache_response
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL, with caching and access counting.

    Parameters:
    url (str): The URL to fetch.

    Returns:
    str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
