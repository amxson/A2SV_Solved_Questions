n,k = map(int,input().split())
arr = list(map(int,input().split()))
cost = []
for i in range(n-1):
    cost.append(arr[i+1]-arr[i])
cost.sort()
tcost = arr[-1]-arr[0]
for i in range(k-1):
    tcost -= cost[-1]
    cost.pop() 
print(tcost)