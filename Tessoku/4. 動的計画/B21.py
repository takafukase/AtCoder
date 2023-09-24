# input
N = int(input())
S = list(input())


if __name__ == "__main__":
    T = list(reversed(S))
    dp = [[0]*(len(T)+1) for _ in range(len(S)+1)]

    for i in range(len(S)+1):
        for j in range(len(T)+1):
            if i < len(S):
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j < len(T):
                dp[i][j+1] = max(dp[i][j+1], dp[i][j])

            if i < len(S) and j < len(T) and S[i] == T[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
    
    print(dp[-1][-1])
