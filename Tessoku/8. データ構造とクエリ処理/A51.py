# import
from collections import deque

# input
Q = int(input())
queries = [input().split() for i in range(Q)] # 0列にクエリ番号、1列に本名

if __name__ == "__main__":
    S = deque()
    for query in queries:
        if query[0] == "1":
            S.append(query[1])
        elif query[0] == "2":
            print(S[-1])
        elif query[0] == "3":
            S.pop()
