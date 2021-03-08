#BOJ 2565 - 전깃줄
n = int(input())
data = []
dp = [1] * n
for _ in range(n):
    data.append(list(map(int,input().split())))
data.sort()
for i in range(n):
    for j in range(i):
        if data[i][1] > data[j][1]:
            dp[i] = max(dp[j]+1,dp[i])
print(n - max(dp))