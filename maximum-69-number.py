class Solution(object):
    def maximum69Number (self, num):
        lnum = list(map(int, str(num)))
        size=len(lnum)
        for i in range(size):
            if lnum[i] == 6:
                lnum[i]=9
                break
        final=  int("".join(map(str,lnum)))
        return final
            
        
