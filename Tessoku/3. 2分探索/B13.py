import itertools

# input
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, 0)

# 2分探索
def search(A, I):
    """
    配列AのI番目以降の要素に対して、function()の2分探索を行う
    """
    L = I + 1
    R = len(A) - 1
    while(L <= R):
        C = (L + R) // 2
        value = function(A, I, C)
        if K == value:
            return C - I
        elif K < value:
            R = C - 1
        elif K > value:
            L = C + 1
    return L - I - 1

def function(A, I, X):
    """
    A: 累積和配列
    I番目からX番目のI番目までの累積和を計算する
    """
    ans = A[X] - A[I]
    return ans

if __name__ == "__main__":
    # 累積和を求める
    cumsum = list(itertools.accumulate(A))

    ans = 0
    for i in range(N):
        ans = ans + search(cumsum, i)
    print(ans)

