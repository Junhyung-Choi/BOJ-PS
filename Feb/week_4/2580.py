#BOJ 2580 - 스도쿠
import sys
from collections import deque
input = sys.stdin.readline

sudoku = []
zeropos = []
ans = []
for i in range(9):
    sudoku.append(list(map(int,input().split())))
for x in range(9):
    for y in range(9):
        if sudoku[x][y] == 0:
            zeropos.append((x,y))

def checkPos(pos,num):
    x,y = pos
    if num in sudoku[x]:
        return False
    for tx in range(9):
        if num == sudoku[tx][y]:
            return False
    ax = (x // 3)*3
    ay = (y // 3)*3
    for dx in range(3):
        for dy in range(3):
            if num == sudoku[ax+dx][ay+dy]:
                return False
    return True

isPrinted = False
def setZero(idx):
    global isPrinted
    if isPrinted:
        return  
    if idx == len(zeropos):
        for i in sudoku:
            print(" ".join(list(map(str,i))))
        isPrinted = True
        return
    else:
        for i in range(1,10):
            if not checkPos(zeropos[idx],i):
                continue
            ans.append((zeropos[idx],i))
            sudoku[zeropos[idx][0]][zeropos[idx][1]] = i
            setZero(idx+1)
            pos,num = ans.pop()
            sudoku[pos[0]][pos[1]] = 0
setZero(0)