class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1 for _ in range(len(nums))]

        #left side multiplications
        pref = 1
        for i in range(len(nums)):
            r[i] = pref
            pref *= nums[i]
        
        #left side multiplications
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            r[i] *= suff
            suff *= nums[i]

        return r