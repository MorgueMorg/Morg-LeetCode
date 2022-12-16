class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_, res = max(candies), []
        for i in candies:
            if i + extraCandies >= max_:
                res.append(True)
            else:
                res.append(False)
        return res