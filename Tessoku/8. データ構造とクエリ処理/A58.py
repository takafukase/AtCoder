# input
N, Q = map(int, input().split())

# 木の初期化
len_of_tree = 3
size = 2
while size < N-1:
    size *= 2
    len_of_tree += size
tree = [0]*(len_of_tree+101)

def search(l, r, a, b, u):
    # l: 調べたい範囲の下限
    # r: 調べたい範囲の上限
    # a: 今見てるノードの範囲の下限
    # b: 今見てるノードの範囲の上限
    # u: 今見てるノード
    if r <= a or b <= l:
        return -10000000000000
    if l <= a and b <= r:
        return tree[u]
    m = (a + b) / 2
    answer_l = search(l, r, a, m, u*2)
    answer_r = search(l, r, m, b, u*2+1)

    return max(answer_l, answer_r)

if __name__ == "__main__":
    # クエリの処理
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            pos = query[1] + size - 1
            tree[pos] = query[2]
            while pos >= 2:
                pos //= 2
                tree[pos] = max(tree[pos*2], tree[pos*2+1])
        elif query[0] == 2:
            print(search(query[1], query[2], 1, size+1, 1))
