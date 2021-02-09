def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
def solution(n, t, m, p):
    ret=''
    ans=''
    for i in range(t*m+1):
        ret+=convert(i,n)
    ret=ret[:t*m]
    for i in range(p-1,t*m,m):
        ans+=ret[i]
    return ans
if __name__ == '__main__':
    n=16
    t=16
    m=2
    p=2
    solution(n, t, m, p)
    