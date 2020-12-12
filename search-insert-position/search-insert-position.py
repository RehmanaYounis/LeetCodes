class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left= 0
        right = len(nums) -1
        mid = (left+right)//2
        while (left<=right):
            if (target == nums[mid]):
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid+1
            mid = (left+right)//2     
        return mid+1
