class Solution(object):
    def numJewelsInStones(self, J, S):
        count=0
        for i in J:
            count=count+S.count(i)
        return count  
        
