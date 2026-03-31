class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # left, right = 0, len(s)-1
        # even string, left right wont overlap
        # odd string, pointers will overlap

        stripped_s = ""
        for char in s:
            if char.isalnum():
                stripped_s += char.lower()

        reverse_str = ""
        for char in s[::-1]:
            if char and char.isalnum():
                reverse_str += char.lower()

        print(stripped_s)
        print(reverse_str)
        return stripped_s == reverse_str

            
    