import heapq
def solution(n, weak, dist):
    answer = 0
    weak_dists=[]# {i} -> dist betw 0 <> 1.. i <> i+1 ... len(weak)-1<>0
    for i in range(len(weak)):
        if i==len(weak)-1:
            weak_dists.append(n-weak[i]+weak[0])
        else:
            weak_dists.append(weak[i+1]-weak[i])
    heapq._heapify_max(weak_dists)
    heapq._heappop_max(weak_dists)
    cur=dist.pop()
    if sum(weak_dists)<=cur:
        return 1
    return answer

if __name__ == '__main__':
    n=12
    weak=[1,3,4,9,10]
    dist=[3,5,7]
    solution(n,weak,dist)
    