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
                continue
            
            if not stack:
                return False
                
            if valid_pair[stack[-1]] != para:
                return False

            stack.pop()
        
        return not stack