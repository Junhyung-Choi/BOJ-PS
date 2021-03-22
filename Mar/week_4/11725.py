#BOJ 11725 - 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline
linenum = int(input())
tree = [[] for _ in range(linenum+1)]
parents = [0] * (linenum + 1)
queue = deque()
for _ in range(linenum-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def findParent():
    queue.append(1)
    while queue:
        tmp = queue.popleft()
        for node in tree[tmp]:
            if parents[node] == 0:
                parents[node] = tmp
                queue.append(node)
findParent()
for index in range(2,linenum+1):
    print(parents[index])
