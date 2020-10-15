import sys,math
import heapq
r=sys.stdin.readline
def midAB(a,b):
    return math.ceil((a+b)/2)
for _ in range(int(r())):
    n=int(r())
    lst=list(range(1,n+1))
    history=[]
    if n==2:
        print(midAB(1,2))
        print("1 2")
    else:
        a=lst.pop(-3)
        b=lst.pop(-1)
        lst.append(midAB(a,b))
        history.append((a,b))
        while len(lst)!=1:
            a=lst.pop()
            b=lst.pop()
            lst.append(midAB(a,b))
            history.append((a,b))
        print(lst[0])
        for a,b in history:
            print(a,b)
