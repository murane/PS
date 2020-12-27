import heapq
def solution(food_times, k):
    answer = 0
    heap=[]
    if sum(food_times)<=k:
        return -1
    for idx,time in enumerate(food_times):
        heapq.heappush(heap,(time,idx+1))
    tot_cnt=0
    cur_cnt=0
    while heap:
        tmp_time,tmp_idx=heapq.heappop(heap)
        tot_cnt+=(tmp_time-cur_cnt)*(len(heap)+1)
        cur_cnt=tmp_time
        if tot_cnt>=k:
            heapq.heappush(heap,(tmp_time,tmp_idx))
            break
    heap.sort(key=lambda x: x[1])
    return heap[(k-tot_cnt)%len(heap)][1]

if __name__ == '__main__':
    #food_times=[4,2,3,6,7,1,5,8]
    #k=27
    food_times=[3,1,2]
    k=1
    answer = 5
    print(solution(food_times, k))
    