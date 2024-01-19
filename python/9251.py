import sys

a=list(sys.stdin.readline().rstrip())

b=list(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

for i in range(len(b)):
    for k in range(len(a)):
        if b[i]==a[k]:
            dp[i+1][k+1] = dp[i][k] +1

        else:
            dp[i + 1][k + 1] = max(dp[i][k+1], dp[i+1][k])


print(dp[-1][-1])