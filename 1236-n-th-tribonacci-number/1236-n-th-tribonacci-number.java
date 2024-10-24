class Solution {
    public int tribonacci(int n) {
        if(n==0){
            return 0;
        }
        else if (n==1 || n==2){
            return 1;
        }
        else{
            int val0 = 0, val1 = 1, val2 = 1;
        
        for (int i = 3; i <= n; i++) {
            int valNext = val0 + val1 + val2;
            val0 = val1;
            val1 = val2;
            val2 = valNext;
        }
        
        return val2;
        }
    }
}