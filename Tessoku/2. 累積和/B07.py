# 入力
T = int(input())
N = int(input())
record = [0]*(T+1)
for i in range(N):
    L, R = map(int, input().split())
    record[L] = record[L] + 1
    record[R] = record[R] - 1

ans = 0
for i in range(T):
    ans = ans + record[i]
    print(ans)