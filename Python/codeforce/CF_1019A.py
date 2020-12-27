import sys
import heapq
from collections import defaultdict
r=sys.stdin.readline
n,m=map(int,r().split())
party_dict=defaultdict(list)
party_heap=[]
party_arr=[]
party_cnt_arr=[0]*(m+1)
for _ in range(n):
    idx,coin=map(int,r().split())
    party_dict[idx].append(coin)
    if idx!=1:
        heapq.heappush(party_heap,(coin,idx))
    party_cnt_arr[idx]+=1
    party_arr.append(((coin,idx)))
party_arr.sort(key=lambda x: x[0])
money=0
mx_cnt=0
lst=[]
for i in range(1,len(party_cnt_arr)):
    if mx_cnt==party_cnt_arr[i]:
        lst.append(i)
    elif mx_cnt<party_cnt_arr[i]:
        lst=[]
        mx_cnt=party_cnt_arr[i]
        lst.append(i)
if 1 in lst:        
    if len(lst)==1:
        print(0)
    else:
        cur,_=heapq.heappop(party_heap)
        print(cur)
else:
    money=0
    if mx_cnt>=len(lst):
        money2=0
        for i in range(mx_cnt+1):
            tmp_money,tmp_idx=heapq.heappop(party_heap)
            money2+=tmp_money
        for i in lst:
            money+=min(party_dict[i])
        j=0
        while j<mx_cnt-len(lst):
            if party_arr[j][1] not in lst:
                money+=party_arr[j][0]
            j+=1
        print(money if money<money2 else money2)
    else:
        for i in range(mx_cnt+1):
            tmp_money,tmp_idx=heapq.heappop(party_heap)
            money+=tmp_money
        print(money)

    
