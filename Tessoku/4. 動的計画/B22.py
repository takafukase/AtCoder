N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
 
if __name__ == "__main__":
    dp = [0]*N
 
    dp[0] = 0
    dp[1] = A[0]
 
    for i in range(2, N):
        if i+1 < N-1:
            dp[i+1] = min(dp[i+1], dp[i]+A[i])
        if i+2 < N-1:
            dp[i+2] = min(dp[i+2], dp[i]+B[i])
 
    print(dp[-1])