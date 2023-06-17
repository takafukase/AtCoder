# input
N, S = map(int, input().split())
A = list(map(int, input().split()))


if __name__ == "__main__":
    ## 動的計画法
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(S+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j + A[i] <= S:
                    dp[i+1][j+A[i]] = True

    if dp[N][S]:
        print("Yes")
    else:
        print("No")


# dp = [[False]*(S+1)]*(N+1)
# で初期化すると、
# dp[0][0] = True
# でdp[1][0]もTrueに変わってしまった...
