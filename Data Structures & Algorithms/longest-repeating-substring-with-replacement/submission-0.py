class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = defaultdict(int)
        f = 0
        l = 0

        for r in range(len(s)):
            c[s[r]] += 1
            f = max(f,c[s[r]])

            if (r-l+1) - f > k:
                c[s[l]] -= 1
                l+=1
        return r-l+1