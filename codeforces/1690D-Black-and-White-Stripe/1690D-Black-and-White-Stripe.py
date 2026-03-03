t =  int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s= input()
    l= 0
    cb = 0
    cw = 0
    ans=float('inf')
    for i in range(len(s)):
        if s[i] == 'W':
            cw += 1
        if i - l + 1 == k:        
            ans = min(ans, cw)
            if s[l] == 'W':         
                cw -= 1
            l+=1
    print(ans)