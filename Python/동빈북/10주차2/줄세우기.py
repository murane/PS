import sys
r=sys.stdin.readline
N=int(r())
line=[]
for _ in range(N):
    line.append(int(r()))
lis=[0]*N
for i in range(len(line)):
    lis[i]=1
    if i!=0:
        for j in range(i):
            #나보다 더크고
            if line[i]>line[j] and lis[j]>=lis[i]:
                lis[i]=lis[j]+1

print(N-max(lis))