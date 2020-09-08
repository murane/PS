import sys
from collections import deque
r=sys.stdin.readline

def is_prinable(documents, imp):
    target=documents[0]
    for num in range(9,target,-1):
        if imp[num]!=0:
            return False
    return True

T=int(r())
for _ in range(T):
    N, M=list(map(int,r().split()))
    documents=deque(list(map(int,r().split())))
    imp=[0]*10
    cnt=0
    cur=M
    for doc in documents:
        imp[doc]+=1
    while True:
        if is_prinable(documents, imp):
            cnt+=1
            if cur==0:
                print(cnt)
                break
            imp[documents[0]]-=1
            documents.popleft()
            cur-=1
        else:
            if cur==0:
                cur=len(documents)-1
            else:
                cur-=1
            documents.rotate(-1)
    
    
    
            

