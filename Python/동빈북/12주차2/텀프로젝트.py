import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**6)
for _ in range(int(r())):
    n=int(r())
    lst=list(map(int,r().split()))
    lst=[x-1 for x in lst]

    def sol(i,s):
        res.append(i)
        if lst[i]==s:
            return True
        else:
            if visit[i]:
                return i
            visit[i]=True
            return sol(lst[i],s)
    cycle=set()
    visit=[False]*(n+1)
    for i in range(n):
        res=[]
        if not visit[i]:
            x = sol(i,i)
            if type(x)==bool and x==True:
                cycle.update(res)
            else:
                res=res[res.index(x)+1:]
                cycle.update(res)

    print(n-len(cycle))

