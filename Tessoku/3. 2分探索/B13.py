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
        j = R
        while j < len(A) and A[j] - A[i-1] <= x:
            j += 1
        ans += j - i
        R = j - 1
    return ans

if __name__ == "__main__":
    # 累積和を求める
    cumsum = list(itertools.accumulate(A))
    ans = two_pointer_technique(cumsum, K)
    print(ans)


"""
テストケース
N, K : 7 50
A : (0) 11 12 16 22 27 28 31
累積和cumsum : 0, 11, 23, 39, 61, 88, 116, 147

考察1
たとえば、3個目から5個目までの和は、
A[3] + A[4] + A[5] = 16 + 22 + 27 = 65
cumsum[5] - cumsum[2] = 65
一般化すると、i番目からj番目までの和は,cumsum[j] - cumsum[i-1]

考察2
たとえば、i = 1のとき、j = 1, 2, 3のとき要素の総和はK(=50)以下である。このとき、小さい要素のインデックスを1とする総和が50以下の組み合わせは、3個ある。

一般化すると、i番目からj番目までの要素の和はK以下で、i番目からj+1番目までの要素の和はKより大きかった。このとき、小さい要素のインデックスをiとする総和がK以下の組み合わせは、(j + 1) - i個ある。
"""
