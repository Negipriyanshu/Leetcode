class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        temp=[]
        for i in range(len(nums1)):
            temp.append(nums2[i]-nums1[i])
            if len(nums1)==1:
                return temp[i]
            if i>0 :
                if temp[i-1] == temp[i]:
                    x=temp[i]
                else:
                    return False
        return x