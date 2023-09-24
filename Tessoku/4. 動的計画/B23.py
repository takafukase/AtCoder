import math
N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]


def d(x1, x2):
   return math.sqrt((x1[0] - x2[0]) ** 2 + (x1[1] - x2[1])**2)


if __name__ == "__main__":
    ## 動的計画法
    dp = [[10000000000]*(2**(N+1)) for _ in range(N+1)]
    dp[1][1] = 0
 
    for i in range(1, N+1):
      for j in range(1, 2**N+1):
        if dp[i][j] < 10000000000:
          for k in range(1, N+1):
            k2 = (1<<(k-1))
            # print(j|k2)
            if j|k2 != j:
              dp[k][j|k2] = min(dp[k][j|k2], dp[i][j]+d(X[i-1], X[k-1]))
              print(dp[k][j|k2])


    if dp[-1][-1] == 10000000:
      print(-1)
    else:
      print(dp[N][2**N-1])