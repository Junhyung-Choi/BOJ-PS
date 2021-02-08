#BOJ 11724 - 연결 요소의 개수
import sys
input = sys.stdin.readline

node,link = map(int,input().split())
matrix = [[0]*node for _ in range(node)]
check = [False] * node
cnt = 0

for _ in range(link):
    da,db = map(int,input().split())
    matrix[da-1][db-1] = matrix[db-1][da-1] = 1 

def bfs(num):
    global cnt
    queue = []
    check[num] = 1
    queue.append(num)
    index = 0
    while index < len(queue):
        tmp = queue[index]
        for i in range(node):
            if matrix[tmp][i] == 1 and not check[i]:
                check[i] = True
                queue.append(i)
        index += 1
    cnt += 1

for i in range(node):
    if not check[i]:
        bfs(i)

print(cnt)