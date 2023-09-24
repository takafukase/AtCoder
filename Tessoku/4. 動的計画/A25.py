H, W = map(int, input().split())
c = [list(map(str, input().split())) for _ in range(H)]

if __name__ == "__main__":
    dp = [[0]*(W) for _ in range(H)]
    dp[0][0] = 1
    print(c[0])
    print(c[1])
    print(c[2])
    print(c[3])

    for i in range(H):
        for j in range(W):
            if c[i][j] != "#":
                if i + 1 < H and c[i+1][j] != "#":
                    dp[i+1][j] += dp[i][j]
                if j + 1 < W and c[i][j+1] != "#":
                    dp[i][j+1] += dp[i][j]
    print(dp)