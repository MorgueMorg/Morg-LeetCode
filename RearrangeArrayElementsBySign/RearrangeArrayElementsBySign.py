class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, res = [], [], []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(0, len(neg)):
            res.append(pos[i])
            res.append(neg[i])
        return res