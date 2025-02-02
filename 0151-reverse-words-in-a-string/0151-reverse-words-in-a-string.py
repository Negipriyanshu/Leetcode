class Solution(object):
    def reverseWords(self, s):
        list1 = s.split()
        reversewords = ''
        for i in list1:
            reversewords= i + " " +reversewords
        return reversewords.strip()