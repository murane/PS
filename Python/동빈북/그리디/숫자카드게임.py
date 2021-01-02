import sys
r=sys.stdin.buffer.readline
N,M=map(int,r().split())
record=[]
for i in range(N):
    lst=list(map(int,r().split()))
    record.append(min(lst))
print(max(record))