from collections import defaultdict

_usage: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))


def record(api_key: str, path: str) -> None:
    _usage[api_key][path] += 1


def usage_for(api_key: str) -> dict[str, int]:
    return dict(_usage.get(api_key, {}))


def reset() -> None:
    _usage.clear()
