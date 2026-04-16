class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ans = 0
        position.sort()
        def check(mm):
            c = 1
            s = position[0]

            for i in position:
                if i-s >= mm:
                    s = i
                    c+=1
            if c>=m:
                return True
            else:
                return False
        l,r = 1,position[-1]-position[0]
        while l<=r:
            mm = l+ (r-l)//2
            if check(mm):
                ans = mm
                l = mm+1
            else:
                r = mm-1
        return ans

        