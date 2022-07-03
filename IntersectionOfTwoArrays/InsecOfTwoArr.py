class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)
        num1.intersection_update(num2)
        return num1


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in nums1:
            if i in nums2:
                arr.append(i)
        return set(arr)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return {i for i in nums1 if i in nums2}


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        arr = []
        for i in nums1:
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] == i:
                    if i not in arr:
                        arr += i,
                    break
                elif nums2[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1
        return arr
