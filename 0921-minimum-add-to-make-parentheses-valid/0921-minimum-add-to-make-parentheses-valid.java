class Solution {
    public int minAddToMakeValid(String s) 
    {
        char[] charArray = s.toCharArray();
        char[] stack1 = new char[s.length()];
        int temp1=s.length(),temp=0;
        if(s.length()>1){
        for(int i=0;i<s.length();i++)
        {
            if(charArray[i]=='(')
            {
                stack1[i]=charArray[i];
                temp++;
            }
            else if(charArray[i]==')' && temp>0)
            {
                if(i>=1 && stack1[temp-1]=='('){
                temp1=temp1-2;
                temp=temp-1;
            }
            }
            else if(charArray[i]==')' && i==0){
                temp1=temp1-2;
            }
            
        }
        return temp1;}
        else {
            return 1;
        }
    }
}