class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        """
        1010
        1011
        """
        if a==0:
            return b
        if b==0:
            return a
        i = len(a)-1
        j = len(b)-1
        res = []
        carry = 0

        while i >= 0 or j >= 0:
            bitA = int(a[i]) if i >= 0 else 0
            bitB = int(b[j]) if j >= 0 else 0
            sum = (bitA + bitB + carry)
            res.append(str(sum % 2))
            carry = sum // 2
            i-=1
            j-=1
        if carry > 0:
            res.append("1")
        res.reverse()
        return "".join(res)