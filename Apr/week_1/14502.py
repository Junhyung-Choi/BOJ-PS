#BOJ 14502 - 연구소
import sys
from collections import deque

input = sys.stdin.readline

matrix = []
queue = deque()
n,m = map(int,input().split())
max_result = 0

for _ in range(n):
    matrix.append(list(map(int,input().split())))

def buildWall(wallnum):
    if wallnum == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                buildWall(wallnum + 1)
                matrix[i][j] = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    global max_result
    tmpmat = [[0] * m for _ in range(n)]
    queue.clear()
    for i in range(n):
        for j in range(m):
            tmpmat[i][j] = matrix[i][j]
            if matrix[i][j] == 2:
                queue.append((i,j))
    result = 0
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmpmat[nx][ny] == 0:
                tmpmat[nx][ny] = 2
                queue.append((nx,ny))
    for i in tmpmat:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(result,max_result)

buildWall(0)
print(max_result)