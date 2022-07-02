class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0]
        for num in nums:
            self.arr.append(self.arr[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right + 1] - self.arr[left]
            
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.n[left:right+1])
            
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)