import sys
import heapq
r=sys.stdin.readline
N=int(r())
total=int(r())
student=set()
heap=[]
for sNum in map(int,r().split()):
    flg=False
    increment=0
    if sNum in student:
        flg=True
        increment=sNum
    elif len(heap)<N:
        student.add(sNum)
        heapq.heappush(heap,(1,0,sNum))  #추천횟수, 게시일, 학생번호
    else:
        a,b,c=heapq.heappop(heap)
        heapq.heappush(heap,(1,0,sNum))
        student.add(sNum)
        student.remove(c)

    tmp=[]
    for item in heap:
        if flg and item[2]==increment:
            tmp.append((item[0]+1,item[1]-1,item[2]))
        else:
            tmp.append((item[0],item[1]-1,item[2]))
    heap=tmp
    heapq.heapify(heap)

#ans=[]
#for item in heap:
#    ans.append(item[2])
#ans.sort()
print(*sorted(student))