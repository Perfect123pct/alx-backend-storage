#!/usr/bin/env python3
"""
Module for implementing an expiring web cache and tracker
"""

import requests
import redis
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()

def cache_and_track(func: Callable) -> Callable:
    """
    Decorator to cache and track the access count of a function with expiration time
    """
    def wrapper(url: str) -> str:
        """
        Wrapper function to cache and track the access count
        """
        # Increment access count
        key_count = f"count:{url}"
        redis_client.incr(key_count)
        
        # Check if URL content is cached
        key_cache = f"cache:{url}"
        cached_content = redis_client.get(key_cache)
        if cached_content:
            return cached_content.decode('utf-8')
        
        # If not cached, fetch content and cache with expiration time
        content = func(url)
        redis_client.setex(key_cache, 10, content)
        return content
    
    return wrapper

@cache_and_track
def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a URL and return it
    Args:
        url (str): The URL to fetch the content from
    Returns:
        str: The HTML content of the URL
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk/delay/10000/url/https://www.example.com"
    print(get_page(url))

