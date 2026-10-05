import asyncio
import functools


def retry(times: int = 3, delay: float = 0.1, exceptions: tuple = (Exception,)):
    def decorator(fn):
        @functools.wraps(fn)
        async def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return await fn(*args, **kwargs)
                except exceptions:
                    if attempt == times - 1:
                        raise
                    await asyncio.sleep(delay * 2**attempt)
        return wrapper
    return decorator
