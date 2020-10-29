import sys
import heapq
r=sys.stdin.readline
N=int(r())
total=int(r())
student=set()
heap=[]
for sNum in map(int,r().split()):
    if sNum in student:
        heap.
    if len(heap)<N:
        student.add(sNum)
        heapq.heappush(heap,(1,0,sNum))  #추천횟수, 게시일, 학생번호
    else:
        heapq.hea
