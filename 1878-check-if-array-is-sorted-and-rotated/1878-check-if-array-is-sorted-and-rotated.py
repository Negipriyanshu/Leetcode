class Solution(object):
    def check(self, nums):
        temp= sorted(nums)
        for i in range(len(nums)):
            last=temp.pop()
            temp.insert(0,last)
            
            if temp == nums :
                return True
        else:
            return False