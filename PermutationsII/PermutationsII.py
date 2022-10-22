class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def recursive(pointer):
            if pointer == len(nums):
                arr.append(nums[:])
                return
            hasht = set()
            for i in range(pointer, len(nums)):
                if nums[i] not in hasht:
                    hasht.add(nums[i])
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    recursive(pointer + 1)
                    nums[i], nums[pointer] = nums[pointer], nums[i]
        recursive(0)
        return arr