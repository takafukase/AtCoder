import bisect
# input
N, L, R = map(int, input().split())
X = [0] + list(map(int, input().split()))

class SegmentTree():
    def __init__(self, n_data, type):
        # 木の初期化
        self.type = type
        self.len_of_tree = 3
        self.size = 2
        while self.size < n_data:
            self.size *= 2
            self.len_of_tree += self.size
        self.tree = [0]*(300000)

    def update(self, index, value):
        pos = index + self.size - 1
        self.tree[pos] = value
        while pos >= 2:
            pos //= 2
            if self.type == 'max':
              self.tree[pos] = max(self.tree[pos*2], self.tree[pos*2+1])
            elif self.type == 'min':
              self.tree[pos] = min(self.tree[pos*2], self.tree[pos*2+1])
        
    def search(self, l, r, a, b, u):
        # l: 調べたい範囲の下限
        # r: 調べたい範囲の上限
        # a: 今見てるノードの範囲の下限
        # b: 今見てるノードの範囲の上限
        # u: 今見てるノード
        if r <= a or b <= l:
            if self.type == 'max':
                return -10000000000000
            elif self.type == 'min':
                return 10000000000000
        if l <= a and b <= r:
            return self.tree[u]
        m = (a + b) / 2
        answer_l = self.search(l, r, a, m, u*2)
        answer_r = self.search(l, r, m, b, u*2+1)

        if self.type == 'max':
            return max(answer_l, answer_r)
        elif self.type == 'min':
            return min(answer_l, answer_r)


if __name__ == "__main__":
    ST = SegmentTree(N, 'min')
    dp = [0]*(N+1)
    ST.update(1, 0)
  
    for i in range(2, N+1):
        posL = bisect.bisect_left(X, X[i] - R)
        posR = bisect.bisect_right(X, X[i]-L)
        if posL == 0:
          posL = 1
        dp[i] = ST.search(posL, posR, 1, ST.size+1, 1) + 1
        ST.update(i, dp[i])
  
    print(dp[N])