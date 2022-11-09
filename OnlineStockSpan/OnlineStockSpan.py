class StockSpanner:

    def __init__(self):
        self.arr = []
        self.lst = []

    def next(self, price: int) -> int:
        if self.arr == []:
            self.arr.append(price)
            self.lst.append(1)
            return 1

        count = 1
        while self.arr:
            if self.arr[-1] <= price:
                count += self.lst.pop()
                self.arr.pop()
            else:
                break

        self.arr.append(price)
        self.lst.append(count)
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)