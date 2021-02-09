import sys
r=sys.stdin.readline
N=r().strip()
l=sum(list(map(int,N[:len(N)//2])))
total=sum(list(map(int,N)))
#입력된 문자열 N의 절반의 합을 두 배 한값이
#전체와 같으면 반반이므로 그대로 처리한다.
if l*2==total:
    print("LUCKY")
else:
    print("READY")
