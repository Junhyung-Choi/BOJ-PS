#BOJ 2667 - 단지번호붙이기
import sys
from collections import deque

input = sys.stdin.readline
size = int(input())
matrix = []
visited = [[0]*size for _ in range(size)]
queue = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = []

for _ in range(size):
    matrix.append(input().rstrip())


def bfs(sx,sy):
    sum = 1
    queue.append((sx,sy))
    visited[sy][sx] = 1
    while queue:
        tmp = queue.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if 0 <= nx < size and 0 <= ny < size and matrix[ny][nx] == '1' and visited[ny][nx] == 0:
                sum += 1
                visited[ny][nx] = 1
                queue.append((nx,ny))
    cnt.append(sum)

for x in range(size):
    for y in range(size):
        if matrix[y][x] == '1' and visited[y][x] == 0:
            queue.clear()
            bfs(x,y)

print(len(cnt))
cnt.sort()
for i in cnt:
    print(i)