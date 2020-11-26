class Solution(object):
    def intersection(self, nums1, nums2):
        set1=set(nums1)
        set2 = set(nums2)
        set3=[]
        for i in set1:
            if i in set2:
               set3.append(i) 
        return set3
