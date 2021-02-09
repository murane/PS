from collections import deque
def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([])
    passed=[]
    answer = 0
    bridge_weight=0
    while len(passed)!=len(truck_weights):
        answer+=1
        if len(trucks)>0 and bridge_weight+trucks[0]<=weight:
            bridge_weight+=trucks[0]
            bridge.append([trucks.popleft(),0])
        if len(bridge)>0:
            for truck in bridge:
                truck[1]+=1
            if bridge[0][1]==bridge_length:
                bridge_weight-=bridge[0][0]
                passed.append(bridge.popleft())
            
    return answer+1

bridge_length=2
weight=10
truck_weights=[7,4,5,6]
print(solution(bridge_length, weight, truck_weights))