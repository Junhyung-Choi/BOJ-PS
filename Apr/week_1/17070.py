#BOJ 17070 - 파이프 옮기기 1
import sys
from collections import deque

input = sys.stdin.readline

matsize = int(input())

matrix = [[1] * (matsize + 1)]

for _ in range(1,matsize+1):
    matrix.append([1] + list(map(int,input().split())))

result = 0

def dfs(x,y,direction):
    global result
    if x == matsize and y == matsize:
        result += 1
        return
    
    if direction == 0 or direction == 2: # 가로, 대각선에서 가로로 바꾸기
        if y + 1 <= matsize and matrix[x][y+1] == 0:
            dfs(x,y+1,0)
    
    if direction == 1 or direction == 2:
        if x + 1 <= matsize and matrix[x+1][y] == 0:
            dfs(x+1,y,1)
    
    if x + 1 <= matsize and y + 1 <= matsize and matrix[x+1][y] == 0 and matrix[x][y+1] == 0 and matrix[x+1][y+1] == 0:
        dfs(x+1,y+1,2)

dfs(1,2,0)
print(result)