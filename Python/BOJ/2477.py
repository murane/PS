import sys
r=sys.stdin.readline
k=int(r())
leng=[]
for _ in range(6):
    a,b=map(int,r().split())
    leng.append(b)
a,b,tmp=0,0,0
for i in range(6):
    if tmp<leng[i]*leng[i-1]:
        a,b=i-1,i
        tmp=leng[i]*leng[i-1]
a=leng[(a+3)%6]
b=leng[(b+3)%6]
res=tmp-a*b
print(res*k)