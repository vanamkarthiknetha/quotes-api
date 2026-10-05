from typing import Generic, Iterable, TypeVar

T = TypeVar("T")


class InMemoryRepository(Generic[T]):
    def __init__(self, items: Iterable[T]):
        self._items: dict[int, T] = {item.id: item for item in items}

    def all(self) -> list[T]:
        return list(self._items.values())

    def get(self, item_id: int) -> T | None:
        return self._items.get(item_id)

    def add(self, item: T) -> T:
        self._items[item.id] = item
        return item

    def count(self) -> int:
        return len(self._items)
