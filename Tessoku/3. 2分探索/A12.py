# 2分探索
def search(K, A):
    L = 0
    R = 10**9
    while(L < R):
        C = (L + R) / 2
        y  = function(C, A)
        if y >= K:
          R = C
        elif y < K:
          L = C + 1
    return L

def function(x, A):
    ans = [int(x/i) for i in A]
    return sum(ans)

if __name__ == "__main__":
    # input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = search(K, A)
    print(int(ans))