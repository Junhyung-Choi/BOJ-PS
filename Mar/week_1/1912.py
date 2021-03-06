#BOJ 1912 - 연속합
n = int(input())
data = list(map(int,input().split()))
max_sum = 0
dp = [0] * n
dp[0] = data[0]
for i in range(1,n):
    dp[i] = max(dp[i-1] + data[i], data[i])
print(max(dp))