class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        arr = []
        for i in stones:
            if i in jewels:
                arr.append(i)
        return len(arr)


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0 
        for i in stones:
            if i in set(jewels):
                count += 1
        return count
        

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count, stones))
        

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)