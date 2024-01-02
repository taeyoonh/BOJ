import sys
from collections import deque

a,b = map(int, sys.stdin.readline().rstrip().split())

gr = deque()
distance=[[-1 for _ in range(b)] for _ in range(a)]
visited=[[False for _ in range(b)] for _ in range(a)]

st=[0,0]
for t in range(a):
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    for tr in range(b):
        if (li[tr]==2):
            k = li.index(2)
            st[0] = t
            st[1] = k
        elif (li[tr]==0):
            distance[t][tr]=0

    gr.append(li)

visited[st[0]][st[1]] = True
distance[st[0]][st[1]] = 0
pr = deque([(st[0], st[1])])
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while pr:
    x1, y1 = pr.popleft()
    for ti in range(4):
        nx = x1 + dx[ti]
        ny = y1+dy[ti]
        if (0<=nx and nx<a and 0<=ny and ny<b):
            if (gr[nx][ny]!=0 and not visited[nx][ny]):
                distance[nx][ny] = distance[x1][y1] + 1
                visited[nx][ny] = True
                pr.append([nx,ny])

for tt in distance:
    print(*tt)