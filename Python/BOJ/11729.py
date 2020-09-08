import sys
r=sys.stdin.readline

def hanoi(n,from_,to,tmp):
    if n==1:
        history.append([from_,to])
    else:
        hanoi(n-1,from_,tmp,to)
        history.append([from_,to])
        hanoi(n-1,tmp,to,from_)

history=[]
N=int(r())
hanoi(N,1,3,2)
print(len(history))
for tup in history:
    print(f'{tup[0]} {tup[1]}')

