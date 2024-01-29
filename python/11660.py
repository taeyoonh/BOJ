import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph=[]

for t in range(n):
    mi = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(mi)

ng=[[0 for _ in range(n)] for _ in range(n)]
ng[0][0]=graph[0][0]

for i in range(n):
    for ii in range(n):
        if i==0 and ii==0:
            pass
        elif i==0:
            ng[i][ii] = ng[i][ii-1] + graph[i][ii]
        elif ii==0:
            ng[i][ii] = ng[i-1][ii] + graph[i][ii]
        else:
            ng[i][ii] = ng[i-1][ii] + ng[i][ii-1] - ng[i-1][ii-1] + graph[i][ii]


for ti in range(m):
    a,b,c,d = map(int, sys.stdin.readline().rstrip().split())
    if a!=1 and b!=1:
        print(ng[c-1][d-1] - ng[c-1][b-2] - ng[a-2][d-1] + ng[a-2][b-2])
    elif a==1 and b!=1:
        print(ng[c - 1][d - 1] - ng[c-1][b-2])
    elif a!=1 and b==1:
        print(ng[c - 1][d - 1] - ng[a-2][d-1])
    else:
        print(ng[c-1][d-1])

