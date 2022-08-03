class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        if end < start:
            return False
        
        i = bisect.bisect_right(self.arr, start)
        if i % 2:
            return False
        
        j = bisect.bisect_left(self.arr, end)
        if i != j:
            return False
        
        self.arr[i:i] = [start, end]
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)