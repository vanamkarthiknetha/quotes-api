import time


class Clock:
    def now(self) -> float:
        return time.time()

    def window_id(self, window_seconds: int) -> int:
        return int(self.now() // window_seconds)

    def seconds_until_next_window(self, window_seconds: int) -> int:
        return int(window_seconds - (self.now() % window_seconds)) or window_seconds


clock = Clock()
