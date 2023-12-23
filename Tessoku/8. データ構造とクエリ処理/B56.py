# input
N, Q = map(int, input().split())
S = list(input())

if __name__ == "__main__":
    mod = 2147483647
    # アルファベットを数字に直す
    alpha2num = lambda c: ord(c) - ord('a') + 1
    S = [alpha2num(c) for c in S]

    # 100のn乗を計算する。あとあと余りが分かればいいのでmodをとる
    B = 100
    Bpower = [1]
    for i in range(1, N+1):
        Bpower.append((Bpower[i-1] * B) % mod)

    # 1文字目からn文字目までのハッシュ値を求める
    H = [0]
    for i in range(1, N+1):
        H.append((H[i-1] * B + S[i-1]) % mod)

    # N文字目からn文字目までのハッシュ値を求める.（逆）
    Hinverse = [0]
    for i in range(1, N+1):
        Hinverse.append((Hinverse[i-1] * B + S[N-i]) % mod)

    # クエリに答える
    for i in range(Q):
        query = list(map(int, input().split()))
        left = H[query[1]] - H[query[0]-1] * Bpower[query[1] - query[0] + 1]
        right = Hinverse[N-query[0]+1] - Hinverse[N-query[1]] * Bpower[query[1] - query[0] + 1]
        if left % mod == right % mod:
            print('Yes')
        else:
            print('No')