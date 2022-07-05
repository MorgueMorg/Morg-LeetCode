class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in nums1:
            if i in nums2:
                arr.append(i)
                nums2.remove(i)
        return arr


class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        arr = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                arr.append(nums1[i])
                i += 1
                j += 1
        return arr