from collections import deque
import heapq
def solution(priorities, location):
    answer = 0
    lst=deque()
    heap=[]
    for i,v in enumerate(priorities):
        lst.append((i,v))
        heap.append(-v)
    heapq.heapify(heap)
    while True:
        if heap[0]==-lst[0][1]:
            answer+=1
            if lst[0][0]==location:
                break
            heapq.heappop(heap)
            lst.popleft()
        else:
            lst.append(lst.popleft())
    return answer
if __name__ == '__main__':
    priorities=[1, 1, 9, 1, 1, 1]
    location=0
    solution(priorities,location)
    