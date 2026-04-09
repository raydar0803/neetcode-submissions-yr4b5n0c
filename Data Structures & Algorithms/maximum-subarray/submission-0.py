class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumSub = nums[0]
        currentSum = 0

        for n in nums: 
            if(currentSum < 0):
                currentSum = 0
            currentSum += n
            maximumSub = max(maximumSub, currentSum)    
        return maximumSub
        