# import
import heapq

# input
Q = int(input())
queries = [input().split() for i in range(Q)] # 0列にクエリ番号、1列に商品の値段

if __name__ == "__main__":
    PQ = []
    for query in queries:
        if query[0] == "1":
            heapq.heappush(PQ, int(query[1]))
        elif query[0] == "2":
            print(PQ[0])
        elif query[0] == "3":
            heapq.heappop(PQ)