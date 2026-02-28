n,s = map(int,input().split())
arr = list(map(int,input().split()))
l= 0
sum =0
count = 0
for r in range(n):
    sum+=arr[r]
    while sum>=s:
        count += (n-r)
        sum-=arr[l]
        l+=1
    
print(count)


