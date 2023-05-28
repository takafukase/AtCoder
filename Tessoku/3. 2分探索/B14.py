import numpy as np
import itertools
import bisect
# input
N, K = map(int, input().split())
A = list(map(int, input().split()))

if __name__ == "__main__":
    ## 前半N//2個までの組み合わせ
    P = []
    for i in range(len(A[0:N//2])+1):
        P = np.concatenate([P, [sum(c) for c in itertools.combinations(A[0:N//2], i)]], 0)
    P.sort()
    ## C, Dの組み合わせ
    Q = []
    for i in range(len(A[N//2:N])+1):
        Q = np.concatenate([Q, [sum(c) for c in itertools.combinations(A[N//2:N], i)]], 0)
    Q.sort()

    ## QにP-Kがあるかを調べる
    fin = False
    for p in P:
        index = bisect.bisect_right(Q, K-p)
        if Q[index-1] == K - p:
            print("Yes")
            fin = True
            break

    if not fin:
        print('No')


"""
テストケース
6 30
5 1 18 7 2 9
output: Yes

Aの前半：A[0:N//2] = [5, 1, 18]
Aの後半：A[N//2:N] = [7, 2, 9]
P = [ 0.  1.  5.  6. 18. 19. 23. 24.]
Q = [ 0.  2.  7.  9.  9. 11. 16. 18.]

コメント1
i個の組み合わせごとにitertools.combinationsを用いて計算する
"""