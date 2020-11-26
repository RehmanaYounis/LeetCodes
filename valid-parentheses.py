class Solution(object):
    def isValid(self, s):
        if len(s) <= 1 or len(s)> 10**4 :
            return False
        
        result = []
        for index, value in enumerate(s):
            if index == 0 and (value == ')' or value == '}' or value == ']'):
                return False
​
            elif value == '(' or value == '{' or value == '[':
                    result.append(value)
                                                 
            elif value == ')'and result !=[]:             
                    if result[-1] == '(':
                        result.pop()
                    else:
                        result.append(value)
            elif value == '}' and result !=[]:
                    if result[-1] == '{':
                        result.pop()
                    else:
                        result.append(value)
            elif value == ']' and result != []:
                    if result[-1] == '[':
                        result.pop()
                    else:
                        result.append(value)
            else:
                    return False
        print(result)
        if result == []:
            return True
        else:
            return False
