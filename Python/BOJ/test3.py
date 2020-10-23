import sys
from collections import deque
input = sys.stdin.readline
n,m,s = map(int,input().split())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
# 첫번째 덱: Ai를 기준으로 정렬한 덱
aa = deque(sorted(arr,key=lambda x: x[0],reverse=True))
# 두번째 덱: Bi를 기준으로 정렬한 덱
bb = deque(sorted(arr,key=lambda x: x[1],reverse=True))
# Ai를 기준으로 한 합계
temp1 = 0
# m만큼 덱에서 temp1에 합함
for i in range(m):
    temp1+=aa[i][0]
# 첫번째 덱: m만큼 덱에서 제거
for i in range(m):
    aa.popleft()
# 첫번째 덱을 Bi를 기준으로 재정렬함
aa = sorted(aa,key=lambda x: x[1],reverse=True)
# s만큼 덱에서 temp1에 합함
for i in range(s):
    temp1+=aa[i][1]
# Bi를 기준으로 한 합계
temp2 = 0
# s만큼 덱에서 temp2에 합함
for i in range(s):
    temp2+=bb[i][1]
# 두번째 덱: s만큼 덱에서 제거
for i in range(s):
    bb.popleft()
# 두번째 덱을 Ai를 기준으로 재정렬함
bb = sorted(bb,key=lambda x: x[0],reverse=True)
# m만큼 덱에서 temp2에 합함
for i in range(m):
    temp2+=bb[i][0]
print(max(temp1,temp2))