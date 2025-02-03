class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sor_list = sorted(nums1+nums2)
        a = len(sor_list)
        if(a%2 == 0):
            temp1 = float(sor_list[(a-1)//2])
            temp2 = float(sor_list[((a-1)//2)+1])
            return (temp1 + temp2)/2
        else:
            return float(sor_list[a//2])

       