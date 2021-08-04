#BOJ 2206 - 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,list(input().strip()))))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visited = [[[0] * 2 for i in range(m)] for i in range(n)]
    visited[0][0][1] = 1
    while queue:
        cx, cy, isbreak = queue.popleft()
        if cx == n - 1 and cy == m - 1:
            return visited[cx][cy][isbreak]
        for i in range(4):
            x = cx + dx[i]
            y = cy + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if matrix[x][y] == 1 and isbreak == 1:
                    visited[x][y][0] = visited[cx][cy][1] + 1
                    queue.append([x, y, 0])
                elif matrix[x][y] == 0 and visited[x][y][isbreak] == 0:
                    visited[x][y][isbreak] = visited[cx][cy][isbreak] + 1
                    queue.append([x, y, isbreak])
    return -1
print(bfs())