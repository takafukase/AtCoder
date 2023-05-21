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
            if A[j] - A[i] > x:
                ans += j - i - 1
                R = j
                break
            elif j == len(A) - 1:
                ans += j - i
                R = j
    return ans

if __name__ == "__main__":
    ans = two_pointer_technique(A, K)
    print(ans)

