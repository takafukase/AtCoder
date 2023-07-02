import copy
# input
N, S = map(int, input().split())
W, V = zip(*[map(int, input().split()) for _ in range(N)])

if __name__ == "__main__":
    ## 動的計画法
    dp = {'0':0}
    next_dp = {'0':0}
    for i in range(N):
        for j in dp:
            j = int(j)
            if j + W[i] <= S:
                if str(j + W[i]) in next_dp:
                    next_dp[str(j+W[i])] = max(next_dp[str(j+W[i])], dp[str(j)] + V[i])
                else:
                    next_dp[str(j+W[i])] = dp[str(j)] + V[i]

        dp = copy.deepcopy(next_dp)
    
    print(max(dp.values()))