
n, S = input().split()
n = int(n)
ans = 0
for i in range(n):
    at, cg = 0, 0
    for s in S[i:n]:
        if s == 'A':
            at += 1
        elif s == 'T':
            at -= 1
        elif s == 'C':
            cg += 1
        else:
            cg -= 1
        if at == cg == 0:
            ans += 1
print(ans)
