#BOJ 10026 - 적록색약
import sys
from collections import deque
input = sys.stdin.readline

size = int(input())
matrix = []
visited = [[0] * size for _ in range(size)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0 

for _ in range(size):
    matrix.append(input().rstrip())

def bfs(start):
    global cnt
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    scolor = matrix[start[0]][start[1]]
    while queue:
        tmp = queue.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if 0 <= nx < size and 0 <= ny < size and visited[nx][ny] == 0 and matrix[nx][ny] == scolor:
                queue.append((nx,ny))
                visited[nx][ny] = 1
    cnt += 1

def rgbfs(start):
    global cnt
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    scolor = matrix[start[0]][start[1]]
    if scolor == "R" or scolor == "G":
        scolor = ["R","G"]
    else:
        scolor = "B"
    while queue:
        tmp = queue.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if 0 <= nx < size and 0 <= ny < size and visited[nx][ny] == 0 and matrix[nx][ny] in scolor:
                queue.append((nx,ny))
                visited[nx][ny] = 1
    cnt += 1

for x in range(size):
    for y in range(size):
        if visited[x][y] == 0:
            bfs((x,y))
print(cnt,end =" ")
visited = [[0] * size for _ in range(size)]
cnt = 0
for x in range(size):
    for y in range(size):
        if visited[x][y] == 0:
            rgbfs((x,y))
print(cnt)

