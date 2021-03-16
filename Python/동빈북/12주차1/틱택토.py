import sys
r=sys.stdin.readline
while True:
    line=list(r().strip())
    if ''.join(line)=="end":
        break
    def ck(ch):
        tmp=0
        if ''.join(line[:3])==ch*3:
            tmp+=1
        if ''.join(line[3:6])==ch*3:
            tmp+=1
        if ''.join(line[6:])==ch*3:
            tmp+=1
        if ''.join([line[i] for i in [0,3,6]])==ch*3:
            tmp+=1
        if ''.join([line[i] for i in [1,4,7]])==ch*3:
            tmp+=1
        if ''.join([line[i] for i in [2,5,8]])==ch*3:
            tmp+=1
        if ''.join([line[i] for i in [0,4,8]])==ch*3:
            tmp+=1
        if ''.join([line[i] for i in [2,4,6]])==ch*3:
            tmp+=1
        return tmp
    def sol(ch):
        origin=ck(ch)
        cnt=0
        for i in range(9):
            if line[i]!=ch:continue
            line[i]='.'
            after=ck(ch)
            if after==0:
                cnt+=1
            line[i]=ch
        if cnt>0:
            return True
        return False
    if line.count('X')-line.count('O') == 0:#마지막이 O
        if not ck('O') and not ck('X') and line.count('.')==0:
            ans = True
        elif ck('O') and not ck('X'):
            ans=sol('O')
        else:
            ans=False
    elif line.count('X')-line.count('O') == 1:#마지막이 X
        if not ck('O') and not ck('X') and line.count('.')==0:
            ans = True
        elif not ck('O') and ck('X'):
            ans=sol('X')
        else:
            ans=False
    else:
        ans=False
    if ans:
        print("valid")
    else:
        print("invalid")
        