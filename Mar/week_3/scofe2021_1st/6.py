#scofe 6 - 시선 이동
import sys
from collections import deque
input = sys.stdin.readline
ysize,xsize = map(int,input().split())
matrix = []
for _ in range(xsize):
    matrix.append(list(map(int,input().split())))
dp = [[0] * (ysize+1) for _ in range(xsize+1)]

for xidx in range(1,xsize+1):
    for yidx in range(1,ysize+1):
        dp[xidx][yidx] = max(dp[xidx-1][yidx],dp[xidx][yidx-1]) + matrix[xidx-1][yidx-1]
print(dp[xsize][ysize])