#!/usr/bin/env python3
"""
Module for retrieving lists
"""

import redis
from typing import Callable, List, Union

class Cache:
    """
    Cache class for storing and retrieving data
    """
    def __init__(self) -> None:
        """
        Initialize the Cache object with a Redis client instance
        """
        self._redis: redis.Redis = redis.Redis()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a randomly generated key
        Args:
            data (Union[str, bytes, int, float]): Data to be stored in Redis

        Returns:
            str: The randomly generated key used for storing the data in Redis
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def replay(self, func: Callable) -> None:
        """
        Display the history of calls of a particular function
        Args:
            func (Callable): The function whose history of calls to be displayed
        """
        keys = self._redis.keys()
        calls: List[str] = []

        for key in keys:
            call_args = self._redis.lrange(key, 0, -1)
            if call_args:
                calls.append(f"{func.__name__}(*{call_args}) -> {key}")

        print(f"{func.__name__} was called {len(calls)} times:")
        for call in calls:
            print(call)

if __name__ == "__main__":
    # Example usage
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    cache.replay(cache.store)

