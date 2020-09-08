import sys
r=sys.stdin.readline
N,M=map(int,r().split())
arr=list(map(int,r().split()))
track=[]
for i,num in enumerate(arr):
    if i==0:
        track.append(num)
    else:
        track.append(num+track[-1])
for _ in range(M):
    i,j=map(int,r().split())
    if i==1:
        print(track[j-1])
    else:
        print(track[j-1]-track[i-2])