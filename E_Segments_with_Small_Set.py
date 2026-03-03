from collections import defaultdict
n,k = map(int,input().split())
arr = list(map(int,input().split()))
dictt = defaultdict(int)
l = 0 
kk = 0
po = 0
for i in range(len(arr)):
    dictt[arr[i]]+=1
    if dictt[arr[i]] == 1:
        kk+=1
    while kk>k:
        dictt[arr[l]]-=1
        if dictt[arr[l]]==0:
            kk-=1
        l+=1
    po+= (i-l+1)
print(po)
    
    
