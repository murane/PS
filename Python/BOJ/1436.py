import sys
r=sys.stdin.readline
N=int(r())
cnt=0
tmp=666
while True:
    if '666' in str(tmp):
        cnt+=1
        if cnt==N:
            print(tmp)
            break
        else:
            tmp+=1
    else:
        tmp+=1