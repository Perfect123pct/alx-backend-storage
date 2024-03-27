#!/usr/bin/env python3
"""
Cache module for storing data in Redis
"""

import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class for storing data in Redis
    """
    def __init__(self) -> None:
        """
        Initialize the Cache object with a Redis client instance and flush the Redis database
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

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

if __name__ == "__main__":
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))

