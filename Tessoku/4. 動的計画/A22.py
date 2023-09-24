N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
 
if __name__ == "__main__":
    dp = [0]*N
    dp[0] = 0
 
    for i in range(0, N-1):
        dp[A[i]-1] = max(dp[A[i]-1], dp[i]+100)
        dp[B[i]-1] = max(dp[B[i]-1], dp[i]+150)
        
        
    print(max(dp))