class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict

        s1_freq_count = defaultdict(int)
        
        for char in s1:
            s1_freq_count[char] += 1
        print(">> s1 freq count", s1_freq_count)

        window_freq_count = defaultdict(int)

        left, right = 0, 0
        while left <= right and right < len(s2):
            window_freq_count[s2[right]] += 1

            if right - left + 1> len(s1):
                window_freq_count[s2[left]] -= 1
            
                if window_freq_count[s2[left]] == 0:
                    window_freq_count.pop(s2[left])
                left += 1

            if s1_freq_count == window_freq_count:
                return True

            print(">> window freq count", window_freq_count)

            right += 1

        return False