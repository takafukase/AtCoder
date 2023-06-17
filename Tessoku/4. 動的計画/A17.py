N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
 
if __name__ == "__main__":
    ## 動的計画法
    dp = [0]*N
    dp[0] = 0
    dp[1] = A[0]
 
    for i in range(2, N):
        dp[i] = min(dp[i-2]+B[i-2], dp[i-1]+A[i-1])
 

    ## ルートを逆算
    place = N - 1
    ans = [place + 1]

    while(place > 0):
        if dp[place] == dp[place-1]+A[place-1]:
            place = place - 1
        else:
            place = place - 2
        ans.append(place + 1)
    ans.reverse()

    print(len(ans))
    print(*ans)