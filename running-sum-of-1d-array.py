class Solution(object):
    def runningSum(self, nums):
        var = 0
        result=[]
        for i in nums:
            var = var + i
            result.append(var)
        return result
