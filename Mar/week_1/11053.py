#BOJ 11053 - 가장 긴 증가하는 부분 수열
n = int(input())
data = list(map(int,input().split()))
dp = [1] * n
for i in range(1,n):
    index = 0
    for j in range(0,i):
        if data[j] < data[i]:
            dp[i] = max(dp[i],dp[j]+1)
#print(dp)
print(max(dp))
