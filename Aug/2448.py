#BOJ 2448 - 별찍기-11
import math

num = int(input())
matrix = [[' '] * 2 * num for _ in range(num)]

def star(x,y,n):
    if n == 3:
        matrix[x][y] = '*'
        matrix[x+1][y-1] = matrix[x+1][y+1] = '*'
        for i in range(-2,3):
            matrix[x+2][y+i] = '*'
    else:
        next = n // 2
        star(x,y,next)
        star(x+next,y-next,next)
        star(x+next,y+next,next)

star(0,num-1,num)
for row in matrix:
    print("".join(row))
