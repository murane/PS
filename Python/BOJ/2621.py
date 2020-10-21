import sys
from collections import Counter
r=sys.stdin.readline
c1=list(r().split())
c2=list(r().split())
c3=list(r().split())
c4=list(r().split())
c5=list(r().split())
colors=[c1[0],c2[0],c3[0],c4[0],c5[0]]
numbers=list(map(int,[c1[1],c2[1],c3[1],c4[1],c5[1]]))
numbers.sort()
counter=Counter(numbers)
numCnt=list(counter.values())
if len(list(set(colors)))==1:
    if list(range(numbers[0],numbers[0]+5))==numbers:
        print(numbers[-1]+900)
    else:
        print(numbers[-1]+600)
elif list(range(numbers[0],numbers[0]+5))==numbers:
    print(numbers[-1]+500)
elif 4 in numCnt:
    for num,cnt in counter.items():
        if cnt==4:
            print(num+800)
            break
elif 3 in numCnt and 2 in numCnt:
    tmp1,tmp2=0,0
    for num,cnt in counter.items():
        if cnt==2:
            tmp1=num
        if cnt==3:
            tmp2=num
    print(tmp2*10+tmp1+700)
elif 3 in numCnt:
    for num,cnt in counter.items():
        if cnt==3:
            print(num+400)
            break
elif numCnt.count(2)==2:
    tmp=[]
    for num,cnt in counter.items():
        if cnt==2:
            tmp.append(num)
    print(max(tmp)*10+min(tmp)+300)
elif numCnt.count(2)==1:
    tmp=0
    for num,cnt in counter.items():
        if cnt==2:
            tmp=num
    print(tmp+200)
else:
    print(numbers[-1]+100)



    
    