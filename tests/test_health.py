def test_health_is_not_limited(get):
    assert {get("/health", {}).status_code for _ in range(20)} == {200}


def test_missing_api_key_is_401(get):
    assert get("/quote", {}).status_code == 401
