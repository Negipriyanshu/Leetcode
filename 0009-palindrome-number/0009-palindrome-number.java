class Solution {
    public boolean isPalindrome(int x)
        {
        int rem=0,num =x, temp = 0;
        if (x >=0)
        {
            if(x==0){
                return true;
            }
        while (num!=0){
            rem=num%10;
            num = (num-rem)/10;        
            temp = temp*10 + rem;
            if (temp == x){
                    return true;
                }
            } 
        } 
           return false;
        }
}