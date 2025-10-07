class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <=1:
            return s
        longest = ""
        for i in range(0, len(s)):
            odd = self.return_palindrome(s, i, i)
            even = self.return_palindrome(s, i, i+1)
            longest = max(longest, odd, even, key=len)
        return longest

    def return_palindrome(self, s, left, right):
        """
        :type s: str
        :type left: int
        :type right: int
        :rtype: str
        """
        while(left >=0 and right < len(s) and s[left]==s[right]):
            left-=1
            right+=1
        return s[left+1:right]
