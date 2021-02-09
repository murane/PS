import sys
r=sys.stdin.readline
S=r().strip()
alpha=[]
num=0
#숫자면 따로 더하고 알파뱃은 저장하여 출력할때 정렬한다.
for ch in S:
    if ch.isdigit():
        num+=int(ch)
    else:
        alpha.append(ch)
print(''.join(sorted(alpha))+str(num))