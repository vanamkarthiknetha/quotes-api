import re

_WORD = re.compile(r"[a-z0-9']+")


def tokenize(text: str) -> list[str]:
    return _WORD.findall(text.lower())


def truncate(text: str, length: int = 80) -> str:
    return text if len(text) <= length else text[: length - 1] + "…"
