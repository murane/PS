import sys
r=sys.stdin.readline
N,K=map(int,r().split())
st=r().strip()
man=[]
eaten=set()
for i,ch in enumerate(st):
    if ch=="P":
        man.append(i)
for i in man:
    for j in range(i-K,i+K+1):
        if 0<=j<N and st[j]=="H" and j not in eaten:
            eaten.add(j)
            break
print(len(eaten))
