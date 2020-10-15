import sys
r=sys.stdin.readline
N=int(r())
switchs=list(map(int,r().split()))
for _ in range(int(r())):
    sex,pos=map(int,r().split())
    if sex==1:#남학생
        for i in range(pos-1,len(switchs),pos):
            switchs[i]=int(not bool(switchs[i]))
    else:#여학생
        if pos-1==0 or pos-1==len(switchs)-1:
            switchs[pos-1]=int(not bool(switchs[pos-1]))
        else:
            a,b=pos-1,pos-1
            while a!=0 and b!=len(switchs)-1:
                a-=1
                b+=1
                if switchs[a]!=switchs[b]:
                    a+=1
                    b-=1
                    break
            for i in range(a,b+1):
                switchs[i]=int(not bool(switchs[i]))

for i in range(1,len(switchs)+1):
    print(switchs[i-1],end=" ")
    if i%20==0:
        print("")
