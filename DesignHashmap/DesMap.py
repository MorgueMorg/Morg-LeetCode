# Не забывать self, из за ООП в задаче
class MyHashMap:
    def __init__(self):
            self.hash_table = [-1]*1000001
    def put(self, key: int, value: int) -> None:
            self.hash_table[key] = value
    def get(self, key: int) -> int:
            return self.hash_table[key]
    def remove(self, key: int) -> None:
            self.hash_table[key] = -1
        
obj = MyHashMap()
obj.put(5, 5)
param_2 = obj.get(5)
obj.remove(5)
