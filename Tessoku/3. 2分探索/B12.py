# 2分探索
def search(N):
    """
    x^3+x=Nを満たす正の実数xを2分探索する
    ただし、誤差は0.001まで許容
    """
    L = 0
    R = N**0.5
    while(L <= R):
        C = (L + R) / 2
        y  = function(C)
        if abs(y-N) <= 0.001:
            return C
        elif y > N:
            R = C
        elif y < N:
            L = C
    return -1

def function(x):
    return x**3+x

if __name__ == "__main__":
    # input
    N = int(input())
    ans = search(N)
    if ans > 0:
        print(ans)
    else:
        print("異常終了")




