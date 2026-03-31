class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_pair = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }

        stack = []
        for para in s:
            if para in valid_pair:
                stack.append(para)
            
            elif not stack:
                return False
            elif valid_pair[stack[-1]] != para:
                return False
            else:
                stack.pop()
            
        return not stack