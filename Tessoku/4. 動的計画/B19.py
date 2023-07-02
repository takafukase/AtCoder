import copy
import numpy as np
# input
N, S = map(int, input().split())
W, V = zip(*[map(int, input().split()) for _ in range(N)])

if __name__ == "__main__":
    ## 動的計画法
    max_value = N*1000
    dp = [[10**10]*(max_value+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(max_value+1):
            if dp[i][j] < 10**10:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
                if dp[i][j] + W[i] <= S:
                    dp[i+1][j+V[i]] = min(dp[i+1][j+V[i]], dp[i][j] + W[i])
    
    ans = [index for index in range(len(dp[-1])) if dp[-1][index] < 10**10]
    print(ans[-1])