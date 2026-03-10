class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_sum = 0
        
        
        for i in range(k):
            window_sum += nums[i]
        
        maximum = window_sum
        
        
        for j in range(k, len(nums)):
            window_sum -= nums[j-k]
            window_sum += nums[j]
            maximum = max(maximum, window_sum)
        
        return maximum / k
        