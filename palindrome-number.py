class Solution(object):
    def isPalindrome(self, x):
        if (x < 0):
            return False
        i = x
        rev= 0
        while(i > 0):
            rev = (rev * 10) + (i % 10)
            i = i//10
        return rev == x
        
