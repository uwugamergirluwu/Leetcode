class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(0, len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if stack and ((s[i]==")" and stack[-1]=="(") or (s[i]=="}" and stack[-1]=="{") or (s[i]=="]" and stack[-1]=="[")):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
            