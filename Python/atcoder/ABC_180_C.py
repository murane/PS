import sys
r=sys.stdin.readline
N=int(r())
divsors=set()
tmp=set()
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        divsors.add(i)
for num in divsors:
    tmp.add(N//num)
for num in sorted(divsors|tmp):
    print(num)