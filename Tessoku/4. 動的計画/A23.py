import math
N = int(input())
X = [[0, 0]]
for _ in range(N):
  X.append(list(map(int, input().split())))

def d(x1, x2):
   return math.sqrt((x1[0] - x2[0]) ** 2 + (x1[1] - x2[1])**2)

if __name__ == "__main__":
    ## 動的計画法
    dp = [[10000000000]*(2**N) for _ in range(N+1)]
    dp[1][1] = 0
    """
    dp[i][j]は、i番目までのクーポンで製品の組み合わせjを
    購入するのに必要なクーポンの最小数を表す。

    """
 
    for i in range(1, N+1):
      for j in range(1, 2**N):
        if dp[i][j] < 10000000000: ## i番目まででjとなる組み合わせが無ければスルー
          for k in range(1, N+1):
            # print(i, j, j|k, j|(1<<(k-1)), k)
            k2 = (1<<(k-1))
            if j|k2 != j:
              print(k2)
              dp[k][j|k2] = min(dp[k][j|k2], dp[i][j]+d(X[i], X[k]))

    for i in range(1, N+1):
        for j in range(1, 2**N):
          if dp[i][j] != 10000000000:
              print(dp[1][2**N-1])