class Solution(object):
    def romanToInt(self, s):
        RDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        addV = 0
        i = 0
        while i < (len(s)):
            if (i < (len(s) - 1)):
                if ((RDic[s[i + 1]] > RDic[s[i]])):
                    addV = RDic[s[i + 1]] - RDic[s[i]]
                    result = result + addV
                    i = i + 2
                else:
                    result = result + RDic[s[i]]
                    i = i + 1
            else:
                result = result + RDic[s[i]]
                i = i+1 
        return result
