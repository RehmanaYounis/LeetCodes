class Solution(object):
    def twoSum(self, nums, target):
        hashT={}
        
        for index,value  in enumerate(nums):
            if (target-value) in hashT:
                return [hashT[target-value], index]
            else:
                hashT[value] = index
         
    
                 
            
