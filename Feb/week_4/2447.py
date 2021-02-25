#BOJ 2447 - 별 찍기 10
import math

size = int(input())
matrix = [["*"] * size for _ in range(size)]

ln = int(round(math.log(size,3)))
def showMat():
    for i in matrix:
        print(''.join(i))

def makeBlank(sx,sy,ln):
    if ln == -1:
        pass
    else:
        # print(sx,sy,ln)
        unit = 3 ** ln
        # print(unit)
        for dx in range(unit):
            for dy in range(unit):
                matrix[sx+unit+dx][sy+unit+dy] = " "
        # print("---------------")
        # showMat()
        # print("---------------")
        makeBlank(sx,sy,ln-1)
        makeBlank(sx,sy+unit,ln-1)
        makeBlank(sx,sy+unit+unit,ln-1)
        makeBlank(sx+unit,sy,ln-1)
        makeBlank(sx+unit,sy+unit+unit,ln-1)
        makeBlank(sx+unit+unit,sy,ln-1)
        makeBlank(sx+unit+unit,sy+unit,ln-1)
        makeBlank(sx+unit+unit,sy+unit+unit,ln-1)

makeBlank(0,0,ln-1)
showMat()
