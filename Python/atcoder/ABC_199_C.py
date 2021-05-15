import sys
r=sys.stdin.readline
N=int(r())
S=r().strip()
Q=int(r())

arr=list(range(2*N))
Rev=False
for _ in range(Q):
    T,A,B=map(int,r().split())
    A=A-1
    B=B-1
    if T==1:
        #정방향
        def swap(a,b):
            arr[a],arr[b]=arr[b],arr[a]
        if not Rev:
            swap(A,B)
        #역방향
        else:
            if 0<=A<N:
                A=A+N
                if 0<=B<N:
                    B=B+N
                else:
                    B=B-N
            else:
                A=A-N
                if 0<=B<N:
                    B=B+N
                else:
                    B=B-N
            swap(A,B)
    else:
        Rev^=True
ans =[S[x] for x in arr]
if not Rev:
    print(''.join(ans))
else:
    print(''.join(ans[N:]+ans[:N]))