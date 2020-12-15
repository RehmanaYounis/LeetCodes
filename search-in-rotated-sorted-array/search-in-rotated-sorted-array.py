class Solution(object):
    def search(self, nums, target):
        
        
        #[2,4,5,6,7,0,1]
        #[5,6,7,0,1,2,4]
        left=0
        right =len(nums)-1
        mid = (left+right)//2
        
        while left<=right:
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target <=nums[mid]:
                    right=mid - 1
                else:
                    left = mid +1
            else:
                if target >= nums[mid] and target <=nums[right]:
                    left=mid + 1
                else:
                    right = mid - 1
            mid = (left+right)//2
                
        return -1
        
           
            
