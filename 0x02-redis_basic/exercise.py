#!/usr/bin/env python3
"""
A module for Redis
"""
import redis
import uuid
from typing import Optional, Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Now write a wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    display call history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        a wrapper funct
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    a function to display the history of
    calls 
    """
    key = method.__qualname__
    redis_cache = redis.Redis()
    input_key = key + ":inputs"
    output_key = key + ":outputs"

    inputs = redis_cache.lrange(input_key, 0, -1)
    outputs = redis_cache.lrange(output_key, 0, -1)

    calls = redis_cache.get(key).decode('utf-8')
    print("{} was called {} times:".format(key, calls))

    for i, o in zip(inputs, outputs):
        i = i.decode('utf-8')
        o = o.decode('utf-8')

        print("{}(*{}) -> {}".format(key, i, o))


class Cache:
    """
    info on redis cache
    """
    def __init__(self) -> None:
        """
        an instance of
        redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        retrn a new uuid after storing data
        """
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """
        get method that take a key
        string argument
        """
        value = self._redis.get(key)

        if value is not None:
            if fn:
                value = fn(value)
            return value
        else:
            return None

    def get_str(self, val: bytes) -> str:
        """
        now return bites in str
        """
        return str(val, val.decode('utf-8'))

    def get_int(self, val: bytes) -> int:
        """
        returns an int
        """
        val = int(val, val.decode('utf-8'))

        return val if val else 0
