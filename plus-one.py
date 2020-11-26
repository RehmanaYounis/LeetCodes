class Solution(object):
    def plusOne(self, digits):
        var=0
        size = len(digits)-1
        for i in range(size,-1,-1):
            var = digits[i]
            var+=1
            if var > 9 and i != 0:
                digits[i]=0
            elif var > 9 and i == 0:
                    digits[i]=0
                    digits.insert(0,1)
            else:
                digits[i]=var
                break
        return digits
        
