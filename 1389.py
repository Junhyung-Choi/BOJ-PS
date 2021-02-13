#BOJ 1389 - 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline

user,btwn = map(int,input().split())
matrix = [[0]*(user+1) for _ in range(user+1)]
bacon = [9999] * (user+1)

for _ in range(btwn):
    usera,userb = map(int,input().split())
    matrix[usera][userb] = 1
    matrix[userb][usera] = 1

def bfs(start):
    visited = [0] * (user + 1)
    visited[start] = 1
    queue = []
    queue.append(start)
    cnt = [0] * (user + 1)
    sum = 0
    while queue:
        tmp = queue.pop(0)
        for i in range(1,user+1):
            if visited[i] == 0 and matrix[tmp][i] == 1:
                cnt[i] = cnt[tmp] + 1
                visited[i] = 1
                queue.append(i)
    for i in cnt:
        sum += i
    bacon[start] = sum

for i in range(1,user+1):
    bfs(i)

print(bacon.index(min(bacon)))