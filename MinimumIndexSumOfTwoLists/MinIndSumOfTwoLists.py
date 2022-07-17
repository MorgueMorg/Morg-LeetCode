class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hasht = set(list1) & set(list2)
        res = {}
        for i in hasht:
            sumIndex = list1.index(i) + list2.index(i)
            res[i] = sumIndex
        temp = min(res.values())
        return [key for key in res if res[key] == temp]