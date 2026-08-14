class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if(s in d):
                d[s].append(strs[i])
            else:
                d[s] = [strs[i]]

        return list(d.values())