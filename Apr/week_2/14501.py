import sys
input = sys.stdin.readline
n = int(input())
timelist = [0] * (n+1)
costlist = [0] * (n+1)
dp = [0] * (n+1)
for i in range(1,n+1):
    time,cost = map(int,input().split())
    timelist[i] = time
    costlist[i] = cost
    dp[i] = cost
for i in range(2,n+1):
    for j in range(1,i):
        if (i - j >= timelist[j]):
            dp[i] = max(costlist[i] + dp[j], dp[i])
result = 0
for i in range(1,n+1):
        if i + timelist[i] <= n + 1:
            if result < dp[i]:
                result = dp[i]
print(result)
