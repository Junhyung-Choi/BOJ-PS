#BOJ 2606 - 바이러스
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

queue = []
node = int(input())
link = int(input())
matrix = [[] for _ in range(node+1)]
checkarr = []
cnt = 0

for _ in range(link):
    i,j = map(int,input().split())
    matrix[i].append(j)
    matrix[j].append(i)

def dfs(node):
    global cnt
    if node not in checkarr:
        checkarr.append(node)
    for cnodeidx in range(len(matrix[node])):
        #if dfscheckarr[matrix[node][cnode]] == False:
        if matrix[node][cnodeidx] not in checkarr:
            dfs(matrix[node][cnodeidx])

def bfs(start):
    checkarr.append(start)
    queue.append(start)
    while queue != []:
        tmp = queue.pop(0)
        for i in matrix[tmp]:
            if i not in checkarr:
                checkarr.append(i)
                queue.append(i)

#Choose DFS or BFS
#dfs(1)
bfs(1)
print(len(checkarr)-1)