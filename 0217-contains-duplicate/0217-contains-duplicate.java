class Solution {
    // using Hashset we can automatically rejects the duplicate elements,while an array list allows duplicate
    public boolean containsDuplicate(int[] nums)
    {
        // Create a HashSet to track seen numbers
    HashSet<Integer> seenNumbers = new HashSet<>();
        
    // Traverse through the array
    for (int num : nums)
        {
        // If the number is already in the set, we found a duplicate
        if (seenNumbers.contains(num))
            {
                return true;
            }
            // Otherwise, add the number to the set
            seenNumbers.add(num);
        }
        
        // If no duplicates were found, return false
        return false;
    }
   
}