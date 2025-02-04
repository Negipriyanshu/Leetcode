class Solution(object):
    def maxAscendingSum(self, nums):
        maxSum = 0
        for i in range(0,len(nums)):
            sum = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] > nums[j-1] :
                    sum = sum + nums[j]
                else:
                    break
            maxSum = max(maxSum,sum)
        return maxSum            
