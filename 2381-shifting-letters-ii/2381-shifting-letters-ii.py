class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0]*n
        for l,r,k in shifts:
            if k == 0:
                shift[l]-=1
                if r+1<n:
                    shift[r+1]+= 1
            else:
                shift[l]+= 1
                if r+1<n:
                    shift[r+1]-=1
        c = 0
        for i in range(len(shift)):
            c+=shift[i]
            shift[i]=c
        ans = []
        for i in range(n):
            num = ord(s[i]) - ord('a') 
            new =  (num + shift[i]) % 26
            ans.append(chr(new + ord('a')))
        return(''.join(ans))



