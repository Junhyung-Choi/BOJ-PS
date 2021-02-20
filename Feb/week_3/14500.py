#BOJ 14500 - 테트로미노
import sys
input = sys.stdin.readline

xlen,ylen = map(int,input().split())

matrix = []
maxarr = []

tet = [[[0,0],[1,0],[2,0],[3,0]],\
       [[0,0],[0,1],[0,2],[0,3]],\
       [[0,0],[1,0],[0,1],[1,1]],\
       [[0,0],[1,0],[2,0],[2,1]],\
       [[0,0],[1,0],[2,0],[2,-1]],\
       [[0,0],[1,0],[0,1],[0,2]],\
       [[0,0],[0,1],[0,2],[1,2]],\
       [[0,0],[0,1],[0,2],[-1,2]],\
       [[0,0],[1,0],[1,1],[1,2]],\
       [[0,0],[1,0],[2,0],[0,1]],\
       [[0,0],[0,1],[1,1],[2,1]],\
       [[0,0],[1,0],[1,1],[2,1]],\
       [[0,0],[0,1],[-1,1],[-1,2]],\
       [[0,0],[0,1],[1,1],[1,2]],\
       [[0,0],[1,0],[0,1],[-1,1]],\
       [[0,0],[0,1],[1,1],[0,2]],\
       [[0,0],[1,0],[1,1],[2,0]],\
       [[0,0],[0,1],[-1,1],[0,2]],\
       [[0,0],[0,1],[-1,1],[1,1]]]
       
for _ in range(xlen):
    matrix.append(list(map(int,input().split())))

def getMax(x,y):
    max_cnt = 0
    for mino in tet:
        cnt = 0
        for node in mino:
            nx = x + node[0]
            ny = y + node[1]
            try:
               cnt += matrix[nx][ny]
            except IndexError:
                break
        max_cnt = max(cnt,max_cnt)
    maxarr.append(max_cnt)
    
for x in range(xlen):
    for y in range(ylen):
        getMax(x,y)

print(max(maxarr))
        


#try:
# except IndexError: