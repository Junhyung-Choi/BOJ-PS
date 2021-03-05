#BOJ 2156 - 포도주 시식
import sys
input = sys.stdin.readline
arr = []
n = int(input())
dp = [0] * (n+1)

for _ in range(n):
    arr.append(int(input()))
dp[1] = arr[0]
if n > 1 :
    dp[2] = arr[0] + arr[1]
if n > 2:
    dp[3] = arr[2] + max(arr[0],arr[1])
for i in range(4,n+1):
    dp[i] = max(dp[i-2], arr[i-2] + dp[i-3], dp[i-4] + arr[i-2]) + arr[i-1]
print(max(dp))