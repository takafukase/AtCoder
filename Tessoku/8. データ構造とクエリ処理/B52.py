# import
from collections import deque

# input
N, X = map(int, input().split())
S = list(input())

if __name__ == "__main__":
    Q = deque()
    Q.append(X-1)
    S[X-1] = '@'
    while (len(Q) > 0):
        pos = Q.popleft()
        if pos-1 >= 0 and S[pos-1] == '.':
            S[pos-1] = '@'
            Q.append(pos-1)
        if pos+1 <= N-1 and S[pos+1] == '.':
            S[pos+1] = '@'
            Q.append(pos+1)
    print(''.join(S))