import bisect

N = int(input())
A = [0]
A = A + list(map(int, input().split()))

if __name__ == "__main__":
    ## 動的計画法
    dp = [N+1]*(N+1)
    L = [500000]*(N+1)
    
    ## 初期化
    dp[1] = 1
    L[0] = 0
    L[1] = A[1]

    for i in range(2, N+1):

        ## L[k] < A[i]となる最大のkを探索する。
        k = bisect.bisect_left(L, A[i])
        dp[i] = k
        L[k] = A[i]

    dp[0] = 0
    print(max(dp))
    
'''
>>> a=[1,2,2,2,3]
>>> 
>>> bisect.bisect_left(a,2)
1
'''