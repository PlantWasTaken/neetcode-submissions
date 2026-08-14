class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        lWall, rWall = 0,0
        s = 0
        
        while l<r:
            if(height[l]<=height[r]): #lWall shorter
                if(height[l] >= lWall): #update wall size
                    lWall = height[l]
                else:
                    s+=lWall-height[l]
                l+=1
            else:
                if(height[r] >= rWall):
                    rWall = height[r]
                else:
                    s+=rWall-height[r]
                r-=1
        return s