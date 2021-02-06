from functools import lru_cache


@lru_cache
def get_env():
    return dict()
