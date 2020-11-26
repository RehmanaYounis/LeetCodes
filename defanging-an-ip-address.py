class Solution(object):
    def defangIPaddr(self, address):
        splitIP=address.split('.')
        finalIP=""
        quater= 0
        for i in splitIP:
            if quater < 3:
                finalIP=finalIP+i+"[.]"
                quater += 1
            else:
                finalIP=finalIP+i
        return finalIP
