#BOJ 7569 - 토마토
import sys
from collections import deque
input = sys.stdin.readline

hor,ver,hgt = map(int,input().split())
queue = deque()

matrix = [[] for b in range(hgt)]
ripday = [[[0] * hor for _ in range(ver)] for i in range(hgt)]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def show(mat):
    for i in mat:
        for j in i:
            print(j)
        print("===========")

for floor in range(hgt):
    for row in range(ver):
        matrix[floor].append(list(map(int,input().split())))

for floor in range(hgt):
    for row in range(ver):
        for tomato in range(hor):
            if matrix[floor][row][tomato] == 1:
                queue.append((tomato,row,floor))

def bfs():
    while queue:
        pos = queue.popleft()
        for i in range(6):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            nz = pos[2] + dz[i]
            if 0 <= nx < hor and 0 <= ny < ver and 0 <= nz < hgt and matrix[nz][ny][nx] == 0:
                queue.append((nx,ny,nz))
                ripday[nz][ny][nx] = ripday[pos[2]][pos[1]][pos[0]] + 1
                matrix[nz][ny][nx] = 1
bfs()
#show(matrix)
#show(ripday)
max = 0
check = True
for floor in range(hgt):
    for row in range(ver):
        for tomato in range(hor):
            if matrix[floor][row][tomato] == 0:
                check = False
                break
            if ripday[floor][row][tomato] > max:
                max = ripday[floor][row][tomato]

if check:
    print(max)
else:
    print(-1)