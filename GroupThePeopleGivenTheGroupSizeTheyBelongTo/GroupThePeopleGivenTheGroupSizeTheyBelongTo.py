class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        arr = []
        hashmap = {}
        for idx, i in enumerate(groupSizes):
            if i not in hashmap:
                hashmap[i]=[idx]
            else:
                hashmap[i].append(idx)
        for key, value in hashmap.items():
            count = 0
            for i in value:
                if count == 0:
                    arr.append([i])
                else:
                    arr[-1].append(i)
                count+=1
                count = count % key
        return arr