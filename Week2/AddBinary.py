class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_bin=(int(a,2))
        b_bin=(int(b,2))
        print(a_bin+b_bin)
        return bin(a_bin+b_bin)[2:]
