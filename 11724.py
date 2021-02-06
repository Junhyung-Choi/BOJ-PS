import sys
input = sys.stdin.readline

dot,line = map(int,input().split())
matrix = [[] for _ in range(dot)]
been = []
cnt = 0

for _ in range(line):
    da,db = map(int,input().split())
    da -= 1
    db -= 1
    matrix[da].append(db)
    matrix[db].append(da)

def bfs(num):
    global cnt
    queue = []
    been.append(num)
    queue.append(num)
    while queue != []:
        tmp = queue.pop(0)
        for i in matrix[tmp]:
            if i not in been:
                been.append(i)
                queue.append(i)
    cnt += 1

for i in range(dot):
    if i not in been:
        bfs(i)
print(cnt)