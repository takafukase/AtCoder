# input
S = list(input())
T = list(input())


if __name__ == "__main__":
    dp = [[100000000]*(len(T)+1) for _ in range(len(S)+1)]
    for i in range(len(S)+1):
        dp[i][0] = i
    for j in range(len(T)+1):
        dp[0][j] = j

    for i in range(len(S)+1):
        for j in range(len(T)+1):
            if i < len(S):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < len(T):
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)

            if i < len(S) and j < len(T):
                c = 0 if S[i] == T[j] else 1
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + c)
    
    
    print(dp[-1][-1])
