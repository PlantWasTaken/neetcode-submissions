class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        return [list(d.keys())[i] for i in range(k)]
