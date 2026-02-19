x = int(input())
arr = list(map(int,input().split()))
arr.sort()
n= len(arr)
c= 0
j = 0
for i in range(1,x+1):
    while j < n and  arr[j]<i:
        j+=1
    if j < n and arr[j]>=i :
        c+=1
        j+=1
    else:
        print(c)
        exit() 
print(c)


