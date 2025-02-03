class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        string1 = ''.join(word1)
        string2=''.join(word2)
        if(string1 == string2):
            return True
        else:
            return False
        