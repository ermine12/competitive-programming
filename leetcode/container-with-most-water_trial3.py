from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        Max = 0
        
        while left < right:
            
            width = right - left
            current = min(height[left], height[right]) * width
            Max = max(Max, current)
            
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return Max
