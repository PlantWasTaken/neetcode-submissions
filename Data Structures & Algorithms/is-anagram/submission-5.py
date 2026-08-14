class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}

        for i in s:
            chars[i] = chars.get(i, 0) + 1

        for i in t:
            chars[i] = chars.get(i, 0) - 1

        for v in chars.values():
            if(v!=0):
                return False
        return True