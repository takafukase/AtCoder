# input
Q = int(input())

if __name__ == "__main__":
    Map = {}
    ans = 0
    for i in range(Q):
        A = int(input())
        if Map.get(A):
            ans += len(Map[A])
            Map[A].appned(i)
        else:
            Map[A] = [i]
    print(ans)
