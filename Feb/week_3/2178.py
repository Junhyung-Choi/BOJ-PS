#BOJ 2178 - 미로 탐색
import sys
from collections import deque

input = sys.stdin.readline

ver,hor = map(int,input().split())
matrix = []
visited = [[0] * hor for _ in range(ver)]
time = [[1] * hor for _ in range(ver)]
queue = deque() 
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(ver):
    matrix.append(input().rstrip())

def bfs(sx,sy):
    queue.append((sx,sy))
    visited[sy][sx] = 1
    while queue:
        tmp = queue.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if 0 <= nx < hor and 0 <= ny < ver and matrix[ny][nx] == '1' and visited[ny][nx] == 0:
                time[ny][nx] = time[tmp[1]][tmp[0]] + 1
                queue.append((nx,ny))
                visited[ny][nx] = 1
bfs(0,0)
print(time[ver-1][hor-1])

