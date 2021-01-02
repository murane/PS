import sys
r=sys.stdin.readline
def count(N):
    cnt=0
    for H in range(N+1):
        for M in range(60):
            for S in range(60):
                if '3' in str(H) or '3' in str(M) or '3' in str(S):
                    cnt+=1
    return cnt
print(count(int(r())))

#최대 60^3 의 시간복잡도를 가짐
#공간사용 x