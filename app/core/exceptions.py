from fastapi import HTTPException, status


class NotFound(HTTPException):
    def __init__(self, what: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=f"{what} not found")


class Unauthorized(HTTPException):
    def __init__(self, detail: str = "Missing or invalid API key"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class RateLimitExceeded(HTTPException):
    def __init__(self, limit: int, retry_after: int):
        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded",
            headers={
                "Retry-After": str(retry_after),
                "X-RateLimit-Limit": str(limit),
                "X-RateLimit-Remaining": "0",
            },
        )
