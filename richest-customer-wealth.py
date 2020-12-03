class Solution(object):
    def maximumWealth(self, accounts):
        #print(len(accounts))
        max_wealth=0   
        temp = 0
        for i in range (len(accounts)):
            for j in range (len(accounts[i])):
                temp = temp +accounts[i][j]
            if max_wealth < temp:
                max_wealth = temp
            temp=0
        return max_wealth
