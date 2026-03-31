class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = []
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            nxt_warmer_temp = 0 
            
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()

            if stack:
                nxt_warmer_temp = stack[-1][0] - i
            
            stack.append((i, temperatures[i]))
            result.append(nxt_warmer_temp)  

        return result[::-1]                              