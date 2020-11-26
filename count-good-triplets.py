class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        size = len(arr)
        for i in range(size - 2):
            for j in range (i+1, size-1):
                for k in range(j+1, size):
                    if ((abs(arr[i]-arr[j])<= a) and (abs(arr[j]-arr[k])<= b) and (abs(arr[i]-arr[k])<= c) ):
                       count += 1
        return count
                        
        
        
