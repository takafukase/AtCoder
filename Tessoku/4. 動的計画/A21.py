# input
N = int(input())
P, A = zip(*[map(int, input().split()) for _ in range(N)])


if __name__ == "__main__":
    dp = [[0]*(N) for _ in range(N)]

    for i in range(N):
        for j in reversed(range(N)):
            if 0 <= j-1:
                if i <= P[j]-1 <= j:
                    dp[i][j-1] = max(dp[i][j] + A[j], dp[i][j-1])
                else:
                    dp[i][j-1] = max(dp[i][j], dp[i][j-1])
            
            if i+1 <= N-1:
                if i <= P[i]-1 <= j:
                    dp[i+1][j] = max(dp[i][j] + A[i], dp[i+1][j]) 
                else:
                    dp[i+1][j] = max(dp[i][j], dp[i+1][j])
    
    ans = 0
    for i in range(N):
        ans = max(ans, dp[i][i])
    print(ans)
