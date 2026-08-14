class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = []

        for i in range(len(s)):
            if(s[i] not in seen):
                seen.append(s[i]) 

            else:
                #early termination
                idx = seen.index(s[i])
                seen = seen[idx+1:]
                seen.append(s[i])
            l=max(len(seen), l)
        return l