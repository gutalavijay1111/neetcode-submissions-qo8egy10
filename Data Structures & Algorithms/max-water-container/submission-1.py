class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = min(heights)
        left, right = 0, len(heights)-1

        while left < right:
            max_area = max(max_area, (right-left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            print(max_area, heights[left], heights[right])

        return max_area    
        