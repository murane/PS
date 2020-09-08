import sys
r=sys.stdin.readline
case=1
while True:
    L,P,V=map(int,r().split())
    if L==0 and P==0 and V==0:
        break
    else:
        #P일중 L일동안 사용할 수 있다.. V일짜리 휴가를 시작...
        div,mod=divmod(V,P)
        #mod = 4 L=5
        if mod<L:
            print(f'Case {case}: {div*L+mod}')
        else:
            print(f'Case {case}: {div*L+L}')
    case+=1