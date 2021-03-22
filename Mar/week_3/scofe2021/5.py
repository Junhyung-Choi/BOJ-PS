#scofe 5 - 시선 이동
import sys
from collections import deque
input = sys.stdin.readline
ysize,xsize = map(int,input().split())
matrix = []
startpoint = []
queue = deque()

for _ in range(xsize):
    matrix.append(input().rstrip())

for idx in range(ysize):
    if matrix[0][idx] == "c":
        startpoint.append([0,idx])

dx = [1,0,0]
dy = [0,-1,1]

def bfs(point):
    queue.append((point))
    visited[point[0]][point[1]] = 1
    while queue:
        tmp = queue.popleft()
        for i in range(3):
            tx = tmp[0]
            ty = tmp[1]
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < xsize and 0 <= ny < ysize and matrix[nx][ny] != 'x' and visited[nx][ny] == 0:
                if dy[i] != 0:
                    time[nx][ny] = time[tx][ty] + 1
                else:
                    time[nx][ny] = time[tx][ty]
                queue.append((nx,ny))
                visited[nx][ny] = 1
    min_move = 123456789
    for idx in range(ysize):
        if visited[xsize-1][idx] == 1:
            min_move = min(min_move,time[xsize-1][idx])
    return min_move


result = 123456789
for point in startpoint:
    queue.clear()
    visited = [[0] * ysize for _ in range(xsize)]
    time = [[0] * ysize for _ in range(xsize)]
    result = min(result,bfs(point))
check = False
for idx in range(ysize):
    if visited[xsize-1][idx] == 1:
        check = True
        break
if check:
    print(result)
else:
    print(-1)
