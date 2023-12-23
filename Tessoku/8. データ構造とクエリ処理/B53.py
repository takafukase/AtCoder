# import
import heapq

# input
N, D = map(int, input().split())
item = {key: [] for key in range(1, D+1)}
for i in range(N):
    x,y=map(int,input().split())
    item[x].append(-1*y)

if __name__ == "__main__":
    PQ = []
    ans = 0
    for d in range(1, D+1):
        for i in item[d]:
            heapq.heappush(PQ, i)
        if PQ:
          ans -= heapq.heappop(PQ)
    print(ans)