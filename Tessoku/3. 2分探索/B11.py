# 2分探索
def search(A, X):
    """
    配列Aに対してXのインデックスを返す
    Xが存在しない場合には、Xより大きい最小値のインデックスを返す
    """
    L = 0
    R = len(A) - 1
    while(L <= R):
        C = (L + R) // 2
        if X == A[C]:
            return C
        elif X < A[C]:
            R = C - 1
        elif X > A[C]:
            L = C + 1
    return L
    

if __name__ == "__main__":
    # input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    A.sort()
    for i in range(Q):
        X = int(input())
        ans = search(A, X)
        print(ans)
