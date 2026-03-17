class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prifix = [0] * n
        
        sum =0
        
        for i in range(n):
            
            sum+=nums[i]
            prifix[i] = sum
        return prifix
        