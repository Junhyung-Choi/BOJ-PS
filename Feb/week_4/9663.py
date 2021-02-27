#BOJ 9663 - N-Queen
from collections import deque

size = int(input())
queenpos = deque()
cnt = 0

def checkPos(nowx,nowy):
    for queen in queenpos:
        qx = queen[0]
        qy = queen[1]
        if nowx == qx or nowy == qy or nowx + nowy == qx + qy or nowx - nowy == qx - qy:
            return False
    return True


def setQueen(row):
    global cnt 
    if len(queenpos) == size:
        cnt += 1
        return
    else:
        for y in range(size):
            if not checkPos(row,y):
                continue
            queenpos.append((row,y))
            setQueen(row+1)
            queenpos.pop()
setQueen(0)
print(cnt)
            