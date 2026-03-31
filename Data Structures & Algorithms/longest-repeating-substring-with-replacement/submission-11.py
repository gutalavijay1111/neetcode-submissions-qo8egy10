class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        freq_map = defaultdict(int)
        
        if len(s) <= 1:
            return len(s)

    #               AAABABB 
    #               |   |
    #               5(len) - 4(A) = 1 < 2(k)     
    # 
        max_sub_len = 0
        left, right = 0,0 
        max_char_freq = 0

        while left <= right and right < len(s):
            
            freq_map[s[right]] += 1
            max_char_freq = max(max_char_freq, freq_map[s[right]])

            window_len = right - left + 1
            if window_len - max_char_freq <= k:
                max_sub_len = max(max_sub_len, window_len)

            else:
                freq_map[s[left]] -= 1                
                left += 1
            
            right += 1

        return max_sub_len








