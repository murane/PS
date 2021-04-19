def solution(m, n, puddles):
    MOD=10**9+7
    dp=[[-1]*m for _ in range(n)]
    dp[0][0]=1
    def get(n,m):
        if dp[n][m]!=-1:
            return dp[n][m]
        if [m+1,n+1] in puddles:
            return 0
        if n==0:
            dp[n][m]=get(n,m-1)
            return dp[n][m]
        elif m==0:
            dp[n][m]=get(n-1,m)
            return dp[n][m]
        dp[n][m]=get(n,m-1)+get(n-1,m)
        return dp[n][m]
    answer=get(n-1,m-1)%MOD
    return answer

if __name__ == '__main__':
    #solution(4,3,[[1, 2], [2, 1]])
    print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨