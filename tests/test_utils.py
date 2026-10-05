from app.ratelimit.keys import build_key, parse_key
from app.utils.hashing import generate_api_key, hash_api_key, verify_api_key
from app.utils.pagination import paginate


def test_key_roundtrip():
    assert parse_key(build_key("abc", 42)) == ("abc", 42)


def test_api_key_hashing():
    key = generate_api_key()
    assert verify_api_key(key, hash_api_key(key))


def test_paginate_clamps():
    page = paginate(list(range(10)), offset=-5, limit=3)
    assert page["items"] == [0, 1, 2] and page["total"] == 10
