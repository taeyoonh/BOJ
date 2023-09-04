import sys
from collections import deque
ni = sys.stdin.readline().rstrip()
n= int(ni)

graph = deque()
counter = deque([[0 for i in range(n)] for j in range(n)])

gdx=[0,1]
gdy=[1, 1]

sdx=[1,1]
sdy=[1,0]

ddx=[1,1,0]
ddy=[0,1,1]

def bfs():
    pos=deque([[0,1,"g"]])
    while (pos):
        #print(pos)
        pi=pos.popleft()
        if pi[2]=="g":
            for i in range(2):
                gxi=pi[0]+gdx[i]
                gyi=pi[1]+gdy[i]
                if (0<=gxi<n and 0<=gyi<n):
                    if (gdx[i]==0):
                        if (graph[gxi][gyi]=="0"):
                            counter[gxi][gyi]+=1
                            pos.append([gxi,gyi,"g"])
                    else:
                        if (graph[gxi][gyi]=="0" and graph[gxi-1][gyi]=="0" and graph[gxi][gyi-1]=="0"):
                            counter[gxi][gyi] += 1
                            pos.append([gxi, gyi, "d"])

        elif pi[2]=="s":
            for j in range(2):
                sxi = pi[0] + sdx[j]
                syi = pi[1] + sdy[j]
                if (0 <= sxi < n and 0 <= syi < n):
                    if (sdy[j] == 0):
                        if (graph[sxi][syi] == "0"):
                            counter[sxi][syi] += 1
                            pos.append([sxi, syi, "s"])
                    else:
                        if (graph[sxi][syi]=="0" and graph[sxi - 1][syi] == "0" and graph[sxi][syi - 1] == "0"):
                            counter[sxi][syi] += 1
                            pos.append([sxi, syi, "d"])
        else:
            for k in range(3):
                dxi = pi[0] + ddx[k]
                dyi = pi[1] + ddy[k]
                if (0 <= dxi < n and 0 <= dyi < n):
                    if (ddy[k] == 0):
                        if (graph[dxi][dyi] == "0"):
                            counter[dxi][dyi] += 1
                            pos.append([dxi, dyi, "s"])
                    elif (ddx[k] == 0):
                        if (graph[dxi][dyi] == "0"):
                            counter[dxi][dyi] += 1
                            pos.append([dxi, dyi, "g"])
                    else:
                        if (graph[dxi][dyi] == "0" and graph[dxi - 1][dyi] == "0" and graph[dxi][dyi - 1] == "0"):
                            counter[dxi][dyi] += 1
                            pos.append([dxi, dyi, "d"])


for i in range(n):
    a=sys.stdin.readline().rstrip().split()
    graph.append(a)

if (graph[n-1][n-1]==0):
    print(0)
    exit()
bfs()
print(counter[n-1][n-1])