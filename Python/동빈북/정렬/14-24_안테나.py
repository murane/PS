import sys
r=sys.stdin.readline
N=int(r())
zib=list(map(int,r().split()))
zib.sort()
lst=[]
#초기 거리의 총합
total=sum(zib)-len(zib)*zib[0]
for i in range(len(zib)):
    if i==0:
        cur=total
    else:
        #증가값과 감소값을 적용
        cur=cur+i*zib[i]-(len(zib)-i)*zib[i]    
    lst.append((zib[i],cur))
lst.sort(key=lambda x: (x[1],x[0]))
print(lst[0][0])