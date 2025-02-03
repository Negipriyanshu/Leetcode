class Solution(object):
    def longestMonotonicSubarray(self, nums):
        maxlen=0
        for i in range(len(nums)):
            length=1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[j-1]:
                    length =length +1
                else:
                    break
            maxlen = max(maxlen,length)
        
            length=1
            for j in range(i+1,len(nums)):
                if nums[j] < nums[j-1]:
                    length=length +1
                else:
                    break
            maxlen= max(maxlen,length)
        return maxlen
        