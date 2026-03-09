class Solution:
    def minOperations(self, logs: List[str]) -> int:
        minm = 0
        for x in logs:
            if x[:-1] == '..':
                if minm >0:
                    minm-=1
                continue
            if x[:-1] == '.' or x[:-1] == '':
                continue
            minm+=1
        return minm