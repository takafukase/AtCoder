# 入力
N = int(input())
X = [None]*N
Y = [None]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
Q = int(input())

# 累積和の計算
matrix = [[0]*1501 for _ in range(1501)]
for i in range(N):
    matrix[Y[i]][X[i]] = matrix[Y[i]][X[i]] + 1

# pypy3だとnumpが使えない...
for y in range(1, 1501):
    for x in range(1, 1501):
        matrix[y][x] = matrix[y][x-1] + matrix[y][x]
 
for y in range(1, 1501):
    for x in range(1, 1501):
        matrix[y][x] = matrix[y-1][x] + matrix[y][x]

for i in range(Q):
    a, b, c, d = map(int, input().split())
    ans = matrix[d][c] - matrix[b-1][c] - matrix[d][a-1] + matrix[b-1][a-1]
    print(ans)