import sys

from collections import deque

n, m, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
graph2 = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

dgraph = [0 for _ in range(n + 1)]
dgraph[0] = -1
dgraph[x] = -1

dgraph2 = [0 for _ in range(n + 1)]
dgraph2[0] = -1
dgraph2[x] = -1
for i in range(m):
    s, e, d = map(int, sys.stdin.readline().rstrip().split())
    graph[s][e] = d
    graph2[e][s] = d

k = deque([x])
k2 = deque([x])

ti = 0
while k:

    st = k.popleft()
    for r in range(n + 1):
        if (r == x or r == 0):
            pass
        else:
            if (graph[st][r] != 0):
                k.append(r)
                if dgraph[r] == 0:
                    if (dgraph[st] < 0):
                        dgraph[r] = graph[st][r]
                    else:
                        dgraph[r] = graph[st][r] + dgraph[st]
                else:
                    dgraph[r] = min(dgraph[r], dgraph[st] + graph[st][r])

    ti += 1
    if (ti == 10000):
        break

tii=0
while k2:

    st = k2.popleft()
    for r in range(n + 1):
        if r == x or r == 0:
            pass
        else:
            if graph2[st][r] != 0:
                k2.append(r)
                if dgraph2[r] == 0:
                    if dgraph2[st] < 0:
                        dgraph2[r] = graph2[st][r]
                    else:
                        dgraph2[r] = graph2[st][r] + dgraph2[st]
                else:
                    dgraph2[r] = min(dgraph2[r], dgraph2[st] + graph2[st][r])

    tii+=1
    if tii==10000:
        break

mini = -1

for xx in range(n + 1):
    mini = max(mini, dgraph2[xx] + dgraph[xx])

print(mini)
