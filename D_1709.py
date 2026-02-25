tests = int(input())
for _ in range(tests):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    opp = []
    def swapa(i):
        arr1[i],arr1[i+1] = arr1[i+1],arr1[i]
        opp.append([1,i])
    def swapb(i):
        arr2[i],arr2[i+1] = arr2[i+1],arr2[i]
        opp.append([2,i])
    def swapab(i):
        arr1[i],arr2[i] = arr2[i],arr1[i]
        opp.append([3,i])
    joint = sorted(arr1+arr2)
    small = set(joint[:n])
    for i in range(n):
        if arr1[i] not in small:
            if arr2[i] in small:
                 swapab(i)
    for i in range(n):
        for j in range(n-1):
            if arr1[j] > arr1[j+1]:
                swapa(j)
            if arr2[j] > arr2[j+1]:
                swapb(j)
    
    print(len(opp))
    for i in opp:
        print(i[0],i[1]+1)

    