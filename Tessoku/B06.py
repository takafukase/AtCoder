import numpy as np

# 入力
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [ None ] * Q
R = [ None ] * Q
for i in range(Q):
	L[i], R[i] = map(int, input().split())
	

# 累積和の配列を作成
cumulative_sum = np.cumsum(A)

# 各問題を解く
for i in range(Q):
	rate = (cumulative_sum[R[i]] - cumulative_sum[L[i]]) / (R[i] - L[i])
	if rate == 0.5:
		print("draw")
	elif rate < 0.5:
		print("lose")
	elif rate > 0.5:
		print("win")