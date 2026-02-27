n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
l = 0
ans = []
for i in range(m):
    while l<n and arr1[l]<arr2[i]:
        l+=1
    ans.append(l)
print(*ans)
    