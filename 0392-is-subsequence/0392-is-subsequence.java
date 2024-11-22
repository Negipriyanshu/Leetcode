class Solution {
public boolean isSubsequence(String s, String t) {
    int temp=0;
    char S[]= s.toCharArray();
    char T[]= t.toCharArray();
    for(int i=0 ;i<S.length;i++)
    {   
        for(int j=0;j<T.length;j++)
        {
            if (S[i] == T[j])
            {
                if(i<S.length-1)
                {
                i++;
                }
                temp =temp+1;
            }
        }
    }
    if (temp == s.length())
        return true ;
    else
        return false;
}
}