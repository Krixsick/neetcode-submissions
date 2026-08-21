class StockSpanner:

    def __init__(self):
        self.s1 = []


    def next(self, price: int) -> int:

        span_total = 1
        while self.s1 and price >= self.s1[-1][0]:
            stock, span = self.s1.pop()
            span_total += span
        self.s1.append([price, span_total])
        return self.s1[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)