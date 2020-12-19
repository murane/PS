def solution(food_times, k):
    time=0
    idx=0
    if sum(food_times)<=k:
        return -1    
    while time<k:
        food_times[idx]-=1
        time+=1
        while True:
            idx=(idx+1)%len(food_times)
            if food_times[idx]>0: break
    return idx+1

if __name__ == '__main__':
    food_times=[3,1,2]
    k=1
    solution(food_times, k)
    