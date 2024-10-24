class Solution(object):
    def minAddToMakeValid(self, s):
        open_bracket =0
        close_bracket =0
        for i in s:
            if i == '(':
                open_bracket = open_bracket+1
            elif i == ')':
                if open_bracket > 0:
                    open_bracket=open_bracket-1
                else :
                    close_bracket=close_bracket+1
        return (open_bracket + close_bracket)
        