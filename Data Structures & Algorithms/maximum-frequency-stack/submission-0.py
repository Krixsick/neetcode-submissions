"""

"""

class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        new_freq = self.freq.get(val, 0) + 1
        self.freq[val] = new_freq
        if new_freq not in self.group:
            self.group[new_freq] = []
        self.group[new_freq].append(val)
        self.maxFreq = max(self.maxFreq, new_freq)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()