from src.exception import MyException
import sys
import functools

def asyncHandler(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        try:
            return await fn(*args, **kwargs)
        except Exception as e:
            raise MyException(e, sys)
    return wrapper

