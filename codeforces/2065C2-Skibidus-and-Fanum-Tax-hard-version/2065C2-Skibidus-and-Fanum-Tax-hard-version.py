from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    prev = -10**18
    ok = True

    for x in a:
        candidates = []

        if x >= prev:
            candidates.append(x)
        idx = bisect_left(b, prev + x)
        if idx < m:
            candidates.append(b[idx] - x)

        if not candidates:
            ok = False
            break

        prev = min(candidates)

    print("YES" if ok else "NO")