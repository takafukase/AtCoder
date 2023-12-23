# input
N, K = map(int, input().split())

def sum_of_digit(number):
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == "__main__":
    dp = [[0]*(N+1) for _ in range(32)]
    A = range(1, N+1)
    # 前処理
    for j in range(0, N):
        dp[0][j+1] = int(A[j])
    for i in range(1, 30):
        for j in range(1, N+1):
            dp[i][j] = dp[i-1][j-sum_of_digit(j)]

    # query処理
    for query in range(1, N+1):
        currentPlace = int(query)
        binary_representation = bin(K)[2:]

        for i, bit in enumerate(reversed(binary_representation)):
            if bit == "1":
                currentPlace = dp[i][currentPlace]

        print(currentPlace)
