n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
l,r = 0,0
count = 0
while l<n and r<m:
    if arr1[l]<arr2[r]:
        l+=1
    elif arr2[r]<arr1[l]:
        r+=1
    else:
        val = arr1[l]
        
        c1 = 0
        while l<n and arr1[l] == val:
            c1+=1
            l+=1
            
        c2 = 0
        while r<m and arr2[r] == val:
            c2+=1
            r+=1
            
        count += c1 * c2
            
print(count)

