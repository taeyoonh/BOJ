import sys
from collections import deque

ai, bi = sys.stdin.readline().rstrip().split()
sys.setrecursionlimit(10**6)

a=int(ai)
b=int(bi)

cnt = 0

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(count,x,y):
    for i in range(4):
        xi=x+dx[i]
        yi=y+dy[i]
        if (0<=xi<a and 0<=yi<b):
            if (graph[xi][yi]==count or graph[xi][yi]==0):
                graph[xi][yi]=count-1
                dfs(count, xi, yi)


def dfsv(x,y):
    if (graph[x][y]==1):
        r=graph[0][0]
        if (graph[x-1][y]==r or graph[x][y-1]==r or graph[x+1][y]==r or graph[x][y+1]==r):
            index_list.append([x,y])

graph = deque()
for i in range(a):
    lim=sys.stdin.readline().rstrip().split()
    li=list(map(int, lim))
    graph.append(li)


lastc=0

while (True):
    index_list = []
    dfs(cnt, 0, 0)
    for ir in range(a):
        for jr in range(b):
            dfsv(ir, jr)
    if (len(index_list)==0):
        print(-cnt)
        break
    lastc=len(index_list)
    for ar, br in index_list:
        graph[ar][br]=graph[0][0]
    cnt-=1

print(lastc)