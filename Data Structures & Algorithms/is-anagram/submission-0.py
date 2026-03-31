class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        from collections import defaultdict
        s_freq_count = defaultdict(int)
        t_freq_count = defaultdict(int)

        for i in range(len(s)):
            s_freq_count[s[i]] += 1
            t_freq_count[t[i]] += 1

        return s_freq_count == t_freq_count