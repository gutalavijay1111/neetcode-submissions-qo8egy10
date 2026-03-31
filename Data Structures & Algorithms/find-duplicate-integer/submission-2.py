class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i, num in enumerate(nums):
            index = abs(num)-1
            if nums[index] < 0:
                return abs(num)

            nums[index] = -nums[index]

        return -1
