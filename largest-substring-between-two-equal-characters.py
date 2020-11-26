class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        ht={}
        temp=''
        secIndex=0
        hvalue = ''
        count=1
        max=0
        for i in range(len(s)):
                    tempStr = s[i+1:len(s)]
                    secIndex=(tempStr.find(s[i]))
                    if secIndex != -1:
                        secIndex=tempStr.rindex(s[i])+count
                        hvalue=s[i+1: secIndex]
                        ht[hvalue]=len(hvalue)
                    count +=1
        for value in ht.values():
            if value > max:
                max=value
        if ht == {}: 
            max =-1
        return (max)
