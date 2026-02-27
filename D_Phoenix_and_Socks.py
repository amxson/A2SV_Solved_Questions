
from collections import Counter
test = int(input())
for _ in range(test):
    n,l,r = map(int,input().split())
    arr = list(map(int,input().split()))
    cost = 0
    left = Counter(arr[:l])
    right = Counter(arr[l:])

    if l>r: 
        while l!=r:
            l-=1
            r+=1
            cost+=1
    elif l<r:
        while l!=r:
            l+=1
            r-=1
            cost+=1
    left = Counter(arr[:l])
    right = Counter(arr[l:])
    dif = left-right
    for i in dif.values():
        cost+=i
    print(cost)







