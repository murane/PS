import sys
r=sys.stdin.readline
def ck(s):
    cnt=0
    lst=[]
    ret=""
    flg=True
    for each in s:
        if each=="?":
            cnt+=1
        elif each=="(":
            if flg:
                flg=False
                ret=each
            lst.append(cnt)
            cnt=0
        else:
            if flg:
                flg=False
                ret=each
            lst.append(cnt)
            cnt=0
    lst.append(cnt)
    return ret,lst
for _ in range(int(r())):
    bra=r().strip()
    cnt=bra.count("?")
    if bra=="()":
        print("YES")
    elif cnt%2!=0 or bra==")(":
        print("NO")
    else:
        x,lst=ck(bra)
        if x=='(':
            print("YES")
        else:
            if lst[0]==0 or lst[2]==0:
                print("NO")
            else:
                print("YES")
    
