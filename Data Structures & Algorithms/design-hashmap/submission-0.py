class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for pair in self.hashmap:
            if key == pair[0]:
                pair[1] = value
                return
        self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for k, value in self.hashmap:
            if k == key:
                return value
        return -1
    def remove(self, key: int) -> None:
        for index, pair in enumerate(self.hashmap):
            if pair[0] == key:
                self.hashmap.pop(index)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)