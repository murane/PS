import heapq
def solution(food_times, k):
    heap=[]
    if sum(food_times)<=k:
        return -1
    for idx,time in enumerate(food_times):
        heapq.heappush(heap,(time,idx+1))
    sum_val=0
    prev=0
    length=len(food_times)
    while sum_val+(heap[0][0]-prev)*length<=k:
        now=heapq.heappop(heap)[0]
        sum_val+=(now-prev)*length
        length-=1
        prev=now
    heap.sort(key=lambda x: x[1])
    return heap[(k-sum_val)%length][1]

if __name__ == '__main__':
    food_times=[4,2,3,6,7,1,5,8]
    k=27
    #food_times=[3,1,2]
    #k=1
    answer = 5
    print(solution(food_times, k))
    