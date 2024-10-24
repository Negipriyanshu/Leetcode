class Solution {
    public int minAddToMakeValid(String s) 
    {   int open=0,close=0;
        char[] charArray = s.toCharArray();
        for(char ch:charArray){
            if (ch=='(')
            {
                open = open +1;
            }
            else if(ch ==')')
            {
                if(open>0)
                {
                    open=open-1;
                }
                else
                {
                    close=close+1;
                }
            }
        }
        return (open + close);
    }
}