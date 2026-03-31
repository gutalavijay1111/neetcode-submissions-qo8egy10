class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        char_found = set()

        left, right = 0,0
        sub_len = 0
        while left <= right and right < len(s):
            if s[right] not in char_found:
                char_found.add(s[right])
                right += 1
                sub_len += 1
            else:
                char_found.remove(s[left])
                left += 1
                sub_len -= 1

            longest = max(longest, sub_len)

        return longest
        
             
