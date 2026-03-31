class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        stripped_s = ""
        for char in s:
            if char.isalnum():
                stripped_s += char.lower()

        return stripped_s == stripped_s[::-1]

            
    