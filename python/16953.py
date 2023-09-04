import sys
from collections import deque

minr=10**9
def bfs(a,b):
    global minr
    c=0
    vr=deque([[a,c]])
    while (vr):

        k=vr.popleft()
        if (k[0]==b):
            minr=min(minr, k[1])

        elif (k[0]<b):
            ki=[k[0]*2, k[1]+1]
            kl=[k[0]*10+1, k[1]+1]
            vr.append(ki)
            vr.append(kl)




a1,b1=sys.stdin.readline().rstrip().split()
a= int(a1)
b= int(b1)

bfs(a,b)
if (minr==10**9):
    print(-1)
else:
    print(minr+1)