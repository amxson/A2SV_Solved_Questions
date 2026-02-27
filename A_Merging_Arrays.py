n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

l,r  = 0,0
ans = []
while l<n and r<m:
    if arr1[l]>arr2[r]:
        ans.append(arr2[r])
        r+=1
    else:
        ans.append(arr1[l])
        l+=1
ans.extend(arr1[l:])
ans.extend(arr2[r:])
print(*ans)


