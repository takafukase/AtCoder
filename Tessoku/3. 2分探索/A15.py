import numpy as np
import itertools
import bisect
import copy
# input
N = int(input())
A = list(map(int, input().split()))

if __name__ == "__main__":

    ans = copy.deepcopy(A)
    ## ユニークな配列Bの作成
    B = list(set(A))
    B.sort()

    for indexA, a in enumerate(A):
        left = bisect.bisect_left(B,a)
        ans[indexA] = left+1
    
    print(*ans)


"""
テストケース
5
46 80 11 77 46
output: 2 4 1 3 2

方針1 (間違い！！)
1. 配列Aのユニークな要素の配列Bを求める。
2. 配列Bをソートする。
3. for文で配列Bから１つずつ要素を取り出し、その要素を配列Aで探す（2分探索）
4. 3で見つけた要素をfor文のイテレーションで置き換える

1. 配列B = [46, 80, 11, 77]
2. 配列B = [11, 46, 77, 80]
3, 4. 配列A = [46, 80, 1, 77, 46]
      配列A = [2, 80, 1, 77, 2]
      配列A = [2, 80, 1, 3, 2]
      配列A = [2, 4, 1, 3, 2]
"""