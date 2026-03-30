import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()
    t = input().strip()

    cnt = [0] * 26
    need = [0] * 26

    for ch in t:
        cnt[ord(ch) - 97] += 1
    for ch in s:
        need[ord(ch) - 97] += 1

    possible = True
    for i in range(26):
        if need[i] > cnt[i]:
            possible = False
            break

    if not possible:
        print("Impossible")
        continue

    ans = []
    p = 0
    m = len(t)

    for _ in range(m):
        for x in range(26):
            if cnt[x] == 0:
                continue

            cnt[x] -= 1
            matched = False

            if p < len(s) and x == ord(s[p]) - 97:
                need[x] -= 1
                matched = True

            ok = True
            for j in range(26):
                if cnt[j] < need[j]:
                    ok = False
                    break

            if ok:
                ans.append(chr(x + 97))
                if matched:
                    p += 1
                break

            cnt[x] += 1
            if matched:
                need[x] += 1

    print(''.join(ans))