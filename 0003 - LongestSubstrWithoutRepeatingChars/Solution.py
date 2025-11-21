class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        chars_index = {}
        start = 0
        longest = 0
        for i, c in enumerate(s):
            if c in chars_index and chars_index[c] >= start:
                start = chars_index[c] + 1
            chars_index[c] = i
            longest = max(longest, i - start + 1)
        return longest
