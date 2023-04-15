# 入力
N = int(input())
count = 0
matrix_size = 1502

matrix = [[0]*matrix_size for _ in range(matrix_size)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    # 走査するときに0始まりなので、+1シフトしておく
    matrix[B+1][A+1] = matrix[B+1][A+1] + 1
    matrix[B+1][C+1] = matrix[B+1][C+1] - 1
    matrix[D+1][A+1] = matrix[D+1][A+1] - 1
    matrix[D+1][C+1] = matrix[D+1][C+1] + 1

# 横に走査
for y in range(1, matrix_size):
    for x in range(1, matrix_size):
      matrix[y][x] = matrix[y][x-1] + matrix[y][x]
# 縦に走査
for y in range(1, matrix_size):
    for x in range(1, matrix_size):
        matrix[y][x] = matrix[y-1][x] + matrix[y][x]
        if matrix[y][x] > 0:
            count = count + 1

print(count)