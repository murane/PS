import sys
r=sys.stdin.readline
T=r().replace('\n',"")
P=r().replace('\n',"")
cnt=0
while True:
    res = T.find(P)
    if res==-1:
        break
    else:
        T=T[res+len(P):]
        cnt+=1
print(cnt)