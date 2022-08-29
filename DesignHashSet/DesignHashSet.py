class MyHashSet:

    def __init__(self):
        self.hash = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hash.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hash)):
            if self.hash[i] == key:
                self.hash.pop(i)
                break

    def contains(self, key: int) -> bool:
        if key in self.hash:
            return True
        else: return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)