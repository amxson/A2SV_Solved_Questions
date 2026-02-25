tests = int(input())
for _ in range(tests):
    n,m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    s = '1543'
    total = 0
    top,bottom = 0,n-1
    left,right = 0,m-1
    while top<=bottom and left<=right:
        data  = ''
        for i in range(left,right+1):
            data+=arr[top][i]
        top+=1
        for i in range(top,bottom+1):
            data+=arr[i][right]
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                data+=arr[bottom][i]
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                data+=arr[i][left]
            left+=1
        data += data[:3]
        for i in range(len(data)-3):
            if data[i:i+4] == s:
                total+=1
    print(total)


