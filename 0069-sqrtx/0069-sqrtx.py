class Solution:
    def mySqrt(self, x):

        if x == 0 or x == 1:
            return x
    
        left, right = 0, x
    
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid
        
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1
    
        return right  



