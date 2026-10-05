FLAGS = {
    "search_v2": True,
    "premium_tier": False,
    "usage_billing": False,
    "response_cache": True,
}


def is_enabled(name: str) -> bool:
    return FLAGS.get(name, False)
