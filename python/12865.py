import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

li =[(0,0)]
for i in range(n):
    ki = list(map(int, sys.stdin.readline().rstrip().split()))
    li.append(ki)


dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for ii in range(1,n+1):
    for tt in range(k+1):
        w = li[ii][0]
        g = li[ii][1]
        if w<=tt:
            dp[ii][tt] = max(dp[ii-1][tt], dp[ii-1][tt-w] +g)
        else:
            dp[ii][tt] = dp[ii-1][tt]

print(dp[n][k])