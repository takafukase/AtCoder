import itertools

# input
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, 0)

def two_pointer_technique(A, x):
    """
    尺取り法
    ソートされた配列Aに対して、条件（差分がx以下になる）を満たす組み合わせを探索する
    """
    ans = 0
    R = 1
    for i in range(1, len(A)):
        for j in range(R, len(A)):
            if A[j] - A[i-1] > x:
                ans += j - i
                R = j - 1
                break
            elif j == len(A) - 1:
                ans += j - i + 1
                R =j
    return ans

if __name__ == "__main__":
    # 累積和を求める
    cumsum = list(itertools.accumulate(A))
    ans = two_pointer_technique(cumsum, K)
    print(ans)

