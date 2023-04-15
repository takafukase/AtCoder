# 入力
N = int(input())
count = 0

matrix = [[0]*1501 for _ in range(1501)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    matrix[B][A] = matrix[B][A] + 1
    matrix[B][C] = matrix[B][C] - 1
    matrix[D][A] = matrix[D][A] - 1
    matrix[D][C] = matrix[D][C] + 1

# 横に走査
for y in range(0, 1500):
    for x in range(0, 1500):
      matrix[y][x] = matrix[y][x-1] + matrix[y][x]
# 縦に走査
for y in range(0, 1500):
    for x in range(0, 1500):
        matrix[y][x] = matrix[y-1][x] + matrix[y][x]
        if matrix[y][x] > 0:
            count = count + 1

print(count)