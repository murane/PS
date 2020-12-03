import sys
from collections import Counter
r=sys.stdin.readline
for _ in range(int(r())):
    n=int(r())
    ans=sys.maxsize
    arr=list(map(int,r().split()))
    counter=Counter()
    nums=set()
    before=0
    for i,num in enumerate(arr):
        if i!=len(arr)-1 and arr[i+1]==arr[i]:
            continue 
        if before!=0 and before!=num:
            #if before not in nums:
            counter[before]+=1
            if num not in nums:
                counter[num]+=1
        nums.add(num)
        before=num
    for num in nums:
        ans=min(ans,counter[num])
    print(ans)