import itertools

# 入力
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [ None ] * Q
R = [ None ] * Q
for i in range(Q):
	L[i], R[i] = map(int, input().split())
	

# 累積和の配列を作成
cumulative_sum = list(itertools.accumulate(A))

# 各問題を解く
for i in range(Q):
	if L[i] == 1:
		rate = cumulative_sum[R[i]-1]/R[i]
	else:
	    rate = (cumulative_sum[R[i]-1] - cumulative_sum[L[i]-2]) / (R[i] - L[i] + 1)
	
	if rate < 0.5:
		print("lose")
	elif rate > 0.5:
		print("win")
	elif rate == 0.5:
		print("draw")