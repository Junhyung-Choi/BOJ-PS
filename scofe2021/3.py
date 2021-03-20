#Scofe 3 - 상품 배치 추천
import sys
input = sys.stdin.readline
matsize = int(input())
matrix = []
for _ in range(matsize):
    matrix.append(list(map(int,input().rstrip())))
num = [0] * matsize
def boolArrange(isize,sx,sy):
    for x in range(sx,sx+isize):
        for y in range(sy,sy+isize):
            if x >= matsize or y >= matsize or matrix[x][y] == 0:
                return False
    return True
for xidx in range(matsize):
    for yidx in range(matsize):
        for arrsize in range(1,matsize+1):
            if matrix[xidx][yidx] == 1 and boolArrange(arrsize,xidx,yidx):
                num[arrsize-1] += 1
print("total: "+str(sum(num)))
for arrsize in range(1,matsize+1):
    if num[arrsize - 1] == 0:
        break
    else:
        print("size["+str(arrsize)+"]: "+str(num[arrsize-1]))
