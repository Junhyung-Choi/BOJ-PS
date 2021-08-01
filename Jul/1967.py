#BOJ 1967 - 트리의 지름
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    dist = [-1] * (nodenumber+1)
    dist[start] = 0
    max_info = [0,0]
    while queue:
        curnode = queue.popleft()
        for child in matrix[curnode]:
            if dist[child[0]] == -1:
                dist[child[0]] = dist[curnode] + child[1]
                queue.append(child[0])
                if dist[child[0]] >= max_info[1]:
                    max_info[0],max_info[1] = child[0],dist[child[0]]
    return max_info

nodenumber = int(input())
matrix = [[] for _ in range(nodenumber+1)]

for _ in range(nodenumber-1):
    pnode,cnode,distance = map(int,input().split())
    matrix[pnode].append((cnode,distance))
    matrix[cnode].append((pnode,distance))

left = bfs(1)
right = bfs(left[0])
print(right[1])
