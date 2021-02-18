#BOJ 11403 - 경로 찾기
import sys
from collections import deque
input = sys.stdin.readline

size = int(input())
matrix = []
visited = [[0] * size for _ in range(size)]

for _ in range(size):
    matrix.append(list(map(int,input().split())))

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        tmp = queue.popleft()
        for link in range(size):
            if visited[start][link] == 0 and matrix[tmp][link] == 1:
                visited[start][link] = 1
                queue.append(link)

for node in range(size):
    bfs(node)

for row in visited:
    for node in row:
        print(node,end = " ")
    print()