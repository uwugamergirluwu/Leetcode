class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote==magazine:
            return True
        ransomCopy = ransomNote
        temp_str = ""
        for i in range(0, len(magazine)):
            if magazine[i] in ransomCopy:
                temp_str+=magazine[i]
                ransomCopy = ransomCopy.replace(magazine[i], "", 1)
                if len(temp_str) == len(ransomNote):
                    return True
        return False