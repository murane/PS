import sys
r = sys.stdin.readline

N, M = list(map(int,r().split()))
cards = list(map(int,r().split()))

tmp=[]
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            sum=cards[i]+cards[j]+cards[k]
            if sum<=M:
                tmp.append(sum)
print(max(tmp))