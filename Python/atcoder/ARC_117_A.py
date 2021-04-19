import sys
r=sys.stdin.readline
A,B=map(int,r().split())
#A개의 양수
#B개의 음수
#sum(arr)==0
#모두 다른 값
#절대값은 10억 내외, 0은 없음
seqA=[x for x in range(1,A+1)]
seqB=[-x for x in range(1,B+1)]
seqB.sort(reverse=True)
if A<B:
    tot=0
    tmpB=[-x for x in seqB]
    while len(tmpB)+1!=A:
        tmp=tmpB.pop()
        tot+=tmp
    tmpB.append(tot)
    print(*(tmpB+seqB))
elif A>B:
    tot=0
    tmpA=[-x for x in seqA]
    while len(tmpA)+1!=B:
        tmp=tmpA.pop()
        tot+=tmp
    tmpA.append(tot)
    print(*(seqA+tmpA))
else:
    print(*(seqA+seqB))

