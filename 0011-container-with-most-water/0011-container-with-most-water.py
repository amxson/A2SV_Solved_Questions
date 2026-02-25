class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,h=0,len(height)-1
        maxx = 0
        minn = 0
        while l<h:
            minn = min(height[l],height[h])
            maxx = max(maxx,(minn*(h-l)))
            if height[l]>height[h]:
                h-=1
            elif height[l]<height[h]:
                l+=1
            else:
                if l+1 < h and height[l+1]<height[h-1]:
                    h-=1
                else:
                    l+=1
        return maxx


        
        