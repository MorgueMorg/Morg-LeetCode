class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for n in nums1:
            idx = nums2.index(n)
            for m in nums2[idx+1:]:
                if m > n:
                    output.append(m)
                    break
            else:
                output.append(-1)
        return output