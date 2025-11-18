class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        right = len(num)-1
        for left in range(0, len(num)):
            if (num[left]!=num[right]):
                return False
            right-=1
        return True
