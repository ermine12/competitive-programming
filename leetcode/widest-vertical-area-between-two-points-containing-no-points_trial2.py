class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_values = []
        for p in points:
            x_values.append(p[0])
        x_values.sort()
        max_gap = 0
        for i in range(1, len(x_values)):
            gap = x_values[i] - x_values[i-1]
            if gap > max_gap:
                max_gap = gap
        return max_gap
    
        