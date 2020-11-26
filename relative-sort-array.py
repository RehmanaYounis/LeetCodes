class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        ht={}
        result=[]
        
        for i in arr1:
            ht[i]=arr1.count(i)
         
        for i in arr2:
            for j in range(ht[i]):
                result.append(i)
            ht.pop(i)
        
        while ht != {}:
            if ht[min(ht)] > 1:
                for i in range (ht[min(ht)]):
                    result.append(min(ht))
                ht.pop(min(ht))
            else:
                result.append(min(ht))
                ht.pop(min(ht))
                
        return result
        
        
        
