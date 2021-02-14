#BOJ 7576 - 토마토
import sys
from collections import deque
input = sys.stdin.readline

hor,ver = map(int,input().split())
matrix = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
day = 0
ripday = [[0] * hor for _ in range(ver)]
dq = deque()

for _ in range(ver):
    matrix.append(list(map(int,input().split())))

for y in range(ver):
    for x in range(hor):
        if matrix[y][x] == 1:
            dq.append([y,x])

while dq:
    y,x = dq.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<= ny < ver and 0 <= nx < hor and matrix[ny][nx] == 0:
            matrix[ny][nx] = 1
            dq.append([ny,nx])
            ripday[ny][nx] = ripday[y][x] + 1

def ans():
    max = 0
    for y in range(ver):
        for x in range(hor):
            if ripday[y][x] > max:
                max = ripday[y][x]
            if matrix[y][x] == 0:
                print(-1)
                return
    print(max)

ans()