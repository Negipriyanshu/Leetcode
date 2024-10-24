class Solution {
public boolean containsDuplicate(int[] nums) 
{
    List<Integer> uniqueList= new ArrayList<>();
    int temp=0;
    for(int i : nums)
        {
         if(!uniqueList.contains(i))
             uniqueList.add(i);
        }
    for(int i : uniqueList)
        {
        for(Integer j : nums)
            {
            if(i == j)
                {
                temp = temp+1;
                if(temp>=2)
                return true;
                }
            }
            temp=0;
        } 
    return false;
 }
}