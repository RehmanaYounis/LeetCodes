class Solution(object):
    def shuffle(self, nums, n):
        num1=0 ; num2= 0
        size= len(nums)
        result=list(([0]*size))
        j = 0
        for i  in range(n):
            result[j]=nums[i]
            result[j+1]= nums[i+n]
            j = j+2
        return result
        
