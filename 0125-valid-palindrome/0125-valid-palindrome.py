class Solution(object):
    def isPalindrome(self, s):
        stack = ""
        for char in s:
            if char.isalnum():
                stack = stack + char.lower()
        return stack == stack[::-1]