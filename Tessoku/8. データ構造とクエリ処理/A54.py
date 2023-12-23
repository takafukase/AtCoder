# input
Q = int(input())
queries = [input().split() for i in range(Q)]

if __name__ == "__main__":
    Map = {}
    for query in queries:
        if query[0] == '1':
            Map[query[1]] = query[2]
        if query[0] == '2':
            print(Map[query[1]])