#BOJ 11051 - 이항계수2
import math
import sys
sys.setrecursionlimit(10 ** 6)
n,k = map(int,input().split())
# print((math.factorial(n) // (math.factorial(k) * math.factorial(n-k))) % 10007)
dp = [[0] * 1001 for _ in range(1001)]
def comb(a,b):
    if dp[a][b] > 0:
        return dp[a][b]
    if b == 0 or a == b:
        dp[a][b] = 1
    else:
        dp[a][b] = comb(a-1,b) + comb(a-1,b-1) 
    return dp[a][b] % 10007
print(comb(n,k))
 