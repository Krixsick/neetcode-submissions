class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        l, r = 0, len(self.map[key]) - 1
        result = ""
        while l <= r:
            middle = (l + r) // 2
            value, prev_time_stamp = self.map[key][middle]
            if prev_time_stamp <= timestamp:
                result = value 
                l = middle + 1
            else:
                r = middle - 1
        return result 

            

