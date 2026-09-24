from collections import deque
class LRUCache:
    """

    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru_cache = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_cache.remove(key)
            self.lru_cache.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru_cache.remove(key)
        elif len(self.cache) >= self.capacity:
            old_key = self.lru_cache.pop(0)
            del self.cache[old_key]

        self.cache[key] = value
        self.lru_cache.append(key)
    


