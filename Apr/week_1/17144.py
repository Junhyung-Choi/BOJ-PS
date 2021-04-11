#BOJ 17144 - 미세먼지 안녕!
import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())

matrix = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(R):
    matrix.append(list(map(int,input().split())))

for x in range(R):
    if matrix[x][0] == -1:
        up = x
        down = x + 1
        break

def expand():
    copy = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if matrix[x][y] >= 5:
                origin = matrix[x][y]
                amount = origin // 5
                for index in range(4):
                    nx = x + dx[index]
                    ny = y + dy[index]
                    if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] != -1:
                        copy[nx][ny] += amount
                        copy[x][y] -= amount
    for x in range(R):
        for y in range(C):
            matrix[x][y] += copy[x][y]
    

def cleaner():
    global up,down
    #UPPER CYCLE
    cx,cy = up - 1, 0
    while True:
        if cy == 0:
            if cx == 0:
                nx,ny = 0,1
            else:
                nx,ny = cx - 1,cy
        elif cx == 0:
            if cy == C - 1:
                nx,ny = 1,C - 1
            else:
                nx,ny = cx,cy + 1
        elif cy == C - 1:
            if cx == up:
                nx,ny = up, cy - 1
            else:
                nx,ny = cx + 1,cy
        elif cx == up:
            nx,ny = cx,cy - 1
        if nx == up and ny == 0:
            matrix[cx][cy] = 0
            break
        else:
            matrix[cx][cy] = matrix[nx][ny]
            cx,cy = nx,ny
    #LOWER CYCLE
    cx,cy = down + 1, 0
    while True:
        if cy == 0:
            if cx == R - 1:
                nx,ny = R -1,1
            else:
                nx,ny = cx + 1,cy
        elif cx == R - 1:
            if cy == C - 1:
                nx,ny = cx - 1 ,C - 1
            else:
                nx,ny = cx,cy + 1
        elif cy == C - 1:
            if cx == down:
                nx,ny = down, cy - 1
            else:
                nx,ny = cx - 1,cy
        elif cx == down:
            nx,ny = cx,cy - 1
        if nx == down and ny == 0:
            matrix[cx][cy] = 0
            break
        else:
            matrix[cx][cy] = matrix[nx][ny]
            cx,cy = nx,ny


for time in range(T):
    expand()
    cleaner()

sum = 0
for x in range(R):
    for y in range(C):
        if matrix[x][y] != -1:
            sum += matrix[x][y]
print(sum)