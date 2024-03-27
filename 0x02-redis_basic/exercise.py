#!/usr/bin/env python3
"""
Cache module for reading from Redis and recovering original type
"""

import redis
from typing import Callable, Optional, Union

class Cache:
    """
    Cache class for reading from Redis and recovering original type
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the given key and optionally apply a conversion function
        Args:
            key (str): The key to retrieve data from Redis
            fn (Optional[Callable]): A conversion function to apply to the retrieved data (default: None)

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data from Redis, optionally converted
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve string data from Redis using the given key
        Args:
            key (str): The key to retrieve string data from Redis

        Returns:
            Optional[str]: The retrieved string data from Redis
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve integer data from Redis using the given key
        Args:
            key (str): The key to retrieve integer data from Redis

        Returns:
            Optional[int]: The retrieved integer data from Redis
        """
        return self.get(key, fn=int)

if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

