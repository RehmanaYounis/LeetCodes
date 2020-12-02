class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        i = 1
        result=[]
        count =0
        TLength = len(target) 
        while count != TLength:
            if i != target[count]:
                result.append("Push")
                result.append("Pop")
            else:
                result.append("Push")
                count=count+1
            i=i+1
        return(result)
