class Solution(object):
    def isPalindrome(self, x):
        temp =str(x)
        temp=temp[::-1]
        if(temp==str(x)):
            return True
        else:
            return False
        