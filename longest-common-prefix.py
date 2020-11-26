class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=''
        j=0
        addLetter=''
        
#Checking if string is empty or has 1 string
        if strs == []:
            return (prefix)
        elif len(strs)==1:
            prefix= strs[0]
            return (prefix)
        
#Checking prefix conditions
        min=len(strs[0])
        for i in range(len(strs)):
            if min > len(strs[i]):
                min = len(strs[i])
#prefix checking        
        for i in range(min):
                for j in range(len(strs)-1):
                    if (strs[j][i] == strs[j+1][i]):
                        addLetter=strs[j][i]
                    else:
                        return prefix
                prefix = prefix + addLetter
        return (prefix)
