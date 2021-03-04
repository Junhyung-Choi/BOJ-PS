#BOJ 10884 - 쉬운 계단  수
MOD = 1000000000
dp = [[0,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,1,1]]
n = int(input())
for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i%2][j] = dp[(i-1)%2][j+1] % MOD
        elif j == 9:
            dp[i%2][j] = dp[(i-1)%2][j-1] % MOD
        else:
            dp[i%2][j] = dp[(i-1)%2][j-1]+dp[(i-1)%2][(j+1)] % MOD
sum = 0
for i in range(10):
    sum += dp[(n-1)%2][i]
print(sum % MOD)