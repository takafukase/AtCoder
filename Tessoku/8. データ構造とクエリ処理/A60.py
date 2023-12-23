# import
from collections import deque
# input
N = int(input())
A = [0] + list(map(int, input().split()))


if __name__ == "__main__":
    ans = [-1]
    st = deque()
    st.append((A[1], 1))
    for i in range(2, N+1):
        # 起算日を求める
        for j in range(len(st)):
            if st[-1][0] <= A[i]:
                st.pop()
            else:
                break
        if len(st) > 0:
            ans.append(st[-1][1])
        elif len(st) == 0:
            ans.append(-1)
        st.append((A[i], i))
    print(*ans)