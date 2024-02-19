import sys
import heapq
n, k = map(int, sys.stdin.readline().rstrip().split())

graph = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(graph, [a,b])
bag = []
for ii in range(k):
    c = int(sys.stdin.readline().rstrip())
    bag.append(c)

bag.sort()

answer = 0
tmp_jew = []
for bagt in bag:
    while graph and bagt >= graph[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(graph)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)

    elif not graph:
        break
print(answer)
