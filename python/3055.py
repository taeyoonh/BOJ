import sys
from collections import deque
a,b = sys.stdin.readline().rstrip().split()
a1=int(a)
b1=int(b)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
graph = deque()
water = deque()
visited = [[0 for i in range(b1)] for j in range(a1)]
startpoint =[]
endpoint=[]

for i in range(a1):
    b=list(sys.stdin.readline().rstrip())
    for s in range(len(b)):
        if (b[s]=="S"):
            startpoint = [i, s]
        if (b[s]=="D"):
            endpoint = [i, s]
        if (b[s]=="*"):
            water.append([i,s])

    graph.append(b)
graph[startpoint[0]][startpoint[1]] = "."

def bfs():
    x1,y1=startpoint
    ti = deque([[x1,y1]])
    while (ti):
        temp=[]
        watermove()
        while (ti):
            x,y = ti.popleft()
            #1. 이부분 왜 쓰는지

            for i in range(4):
                xi = x+dx[i]
                yi=  y+dy[i]
                if (0<=xi<a1 and 0<=yi<b1):
                    if (graph[xi][yi]=="." and visited[xi][yi]==0):
                        visited[xi][yi]=visited[x][y]+1
                        temp.append([xi, yi])
                    elif (graph[xi][yi] == "D" and visited[xi][yi] == 0):
                        return visited[x][y]+1
        for ar,br in temp:
            ti.append([ar,br])


    return "KAKTUS"


def watermove():
    new_water=[]
    while water:
        t1,t2=water.popleft()
        for i in range(4):
            tx = t1+dx[i]
            ty = t2+dy[i]
            if (0<=tx<a1 and 0<=ty<b1):
                if (graph[tx][ty]=="."):
                    graph[tx][ty]="*"
                    new_water.append([tx,ty])
    for ai, bi in new_water:
        water.append([ai,bi])

print(bfs())

