class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_found = 0
        nums_found = set()

        for num in nums:
            if num not in nums_found:
                nums_found.add(num)

            sequence_length = 1
            next_left_element = num - 1 
            next_right_element = num + 1 

            # left sequence
            while next_left_element in nums_found:
                sequence_length += 1
                next_left_element -= 1 

            # right sequence
            while next_right_element in nums_found:
                sequence_length += 1
                next_right_element += 1 

            max_found = max(max_found, sequence_length)

        return max_found