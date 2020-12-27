import heapq
def solution(food_times, k):
    answer = 0
    heap=[]
    if sum(food_times)<=k:
        return -1
    for idx,time in enumerate(food_times):
        heapq.heappush(heap,(time,idx+1))
    consumed_food_cnt=0
    
        
    return answer