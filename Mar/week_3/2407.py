#BOJ 2407 - 조합
from math import factorial
dp = [[0] * 101 for _ in range(101)]
n,m = map(int,input().split())

def comb(a,b):
    if b == 0 or a == b:
        dp[a][b] = 1
        return dp[a][b]
    elif dp[a][b] != 0:
        return dp[a][b]
    else:
        dp[a][b] = comb(a-1,b) + comb(a-1,b-1)
    return dp[a][b]

print(comb(n,m))