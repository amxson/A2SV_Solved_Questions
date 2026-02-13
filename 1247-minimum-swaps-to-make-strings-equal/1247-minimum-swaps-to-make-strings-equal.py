class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        chan = 0
        xy = 0
        yx= 0
        for i,j in zip(s1,s2):
            if i == j:
                continue
            if i+j == 'xy':
                xy +=1
            if i + j=='yx':
                yx+=1
        
        if (xy+yx)%2 != 0 :
            return -1
        
        if xy%2!=0:
            chan+=(xy+yx-2)//2
            chan+=2
        else:
            chan+=(xy+yx)//2
        return chan

        
        