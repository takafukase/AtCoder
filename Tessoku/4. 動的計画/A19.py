# input
N, S = map(int, input().split())
W, V = zip(*[map(int, input().split()) for _ in range(N)])

if __name__ == "__main__":
    ## 動的計画法
    dp = [[-1]*(S+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(S+1):
            if dp[i][j] >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                if j + W[i] <= S:
                    dp[i+1][j+W[i]] = max(dp[i+1][j+W[i]], dp[i][j] + V[i])
    
    print(max(dp[-1]))