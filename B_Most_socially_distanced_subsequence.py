test = int(input())
for _ in range(test):
    n= int(input())
    arr = list(map(int, input().split()))
    l,r = 0, 1
    ans = []
    ans.append(arr[l])
    while r<n:   
        if arr[l]<arr[r]:
            while r<n and arr[r-1]<arr[r]:
                r+=1
            l=r-1
            ans.append(arr[l])
            
        else:
            while r<n and arr[r-1]>arr[r]:
                r+=1
            l=r-1
            ans.append(arr[l])
            
    print(len(ans))
    print(*ans)
            
            
            




            


        
