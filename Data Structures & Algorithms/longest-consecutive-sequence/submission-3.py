class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_seq = 0
        nums_found = set(nums) #removing duplicates

        for num in nums:
            if num - 1 not in nums_found:
                seq_length = 1
                while num + 1 in nums_found:
                    seq_length += 1
                    num += 1
                
                max_seq = max(max_seq, seq_length)
        
        return max_seq
            