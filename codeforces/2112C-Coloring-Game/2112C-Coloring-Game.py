import sys
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    maxx = arr[-1]
    ans = 0
    for i in range(2,n):
        mx = max(arr[i], maxx-arr[i])
        l = 0
        j = i-1
        while l<j:
            if arr[l]+arr[j]>mx:
                ans += j-l
                j-=1
            else:
                l+=1
    print(ans)