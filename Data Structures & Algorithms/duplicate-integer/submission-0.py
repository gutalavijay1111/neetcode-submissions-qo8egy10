class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values_found = set()
        for num in nums:
            if num in values_found:
                return True
            values_found.add(num)
        return False