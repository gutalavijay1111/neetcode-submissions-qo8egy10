class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_found = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums_found:
                return [nums_found[remainder], i]
            nums_found[nums[i]] = i

        

