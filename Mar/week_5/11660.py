#BOJ 11660 - 구간 합 구하기 5
import sys
input = sys.stdin.readline

matsize, t_case = map(int,input().split())
matrix = [[0] * (matsize +1)]
for _ in range(matsize):
    matrix.append([0] + list(map(int,input().split())))

dp = [[0] * (matsize+1) for _ in range(matsize+1)]

for x in range(1,matsize+1):
    cursum = 0
    for y in range(1,matsize+1):
        cursum += matrix[x][y]
        dp[x][y] = dp[x-1][y] + cursum

for _ in range(t_case):
    sx,sy,ex,ey = map(int,input().split())
    result = dp[ex][ey] - dp[sx-1][ey] - dp[ex][sy-1] + dp[sx-1][sy-1]
    print(result)  