#!/usr/bin/env python3
"""
Cache module
"""

import redis
import uuid
from typing import Any, Callable, Optional
from typing import Union
from functools import wraps

class Cache:
    """
    Cache class for storing data in Redis
    """

    def __init__(self) -> None:
        """
        Initializes the Cache instance with a Redis client and flushes the database.
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis with a random key and returns the key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key used for storing the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

if __name__ == "__main__":
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))

class Cache:
    """
    A class to interact with Redis cache.

    Methods:
    store(value: Union[str, int, bytes]) -> str: Store a value in the cache and return its key.
    get(key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any: Retrieve a value from the cache using its key,
                                                                    optionally applying a conversion function.
    get_str(key: str) -> str: Retrieve a string value from the cache.
    get_int(key: str) -> int: Retrieve an integer value from the cache.
    """

    def __init__(self) -> None:
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)

    def store(self, value: Any) -> str:
        """Store a value in the cache and return its key."""
        key = self.redis_client.incr('key_counter')
        self.redis_client.set(str(key), value)
        return str(key)

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """
        Retrieve a value from the cache using its key,
        optionally applying a conversion function.
        """
        value = self.redis_client.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """Retrieve a string value from the cache."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve an integer value from the cache."""
        return self.get(key, fn=lambda d: int(d))


# Test
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

class Cache:
    """
    A class to interact with Redis cache.

    Methods:
    store(value: Any) -> str: Store a value in the cache and return its key.
    get(key: str) -> Any: Retrieve a value from the cache using its key.
    """

    def __init__(self) -> None:
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count how many times methods of the Cache class are called.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs) -> Any:
            key = method.__qualname__
            self.redis_client.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, value: Any) -> str:
        """Store a value in the cache and return its key."""
        key = self.redis_client.incr('key_counter')
        self.redis_client.set(str(key), value)
        return str(key)

    def get(self, key: str) -> Any:
        """Retrieve a value from the cache using its key."""
        return self.redis_client.get(key)


# Test
if __name__ == "__main__":
    cache = Cache()

    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))

