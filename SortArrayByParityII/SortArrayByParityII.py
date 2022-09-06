class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_arr = []
        odd_arr = []
        for i in nums:
            if i % 2 == 0:
                even_arr.append(i)
            else:
                odd_arr.append(i)
        nums.clear()
        for j in range(len(even_arr)):
            nums.append(even_arr[j])
            nums.append(odd_arr[j])
        return nums