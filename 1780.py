#BOJ 1780 - 종이의 개수

import sys
input = sys.stdin.readline
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

p,z,m = 0,0,0

def nineRecur(sx,sy,size):
    global p,z,m
    tmp = 0
    check = True
    before = matrix[sy][sx]
    for i in range(sx,sx+size):
        for j in range(sy,sy+size):
            if check and before != matrix[j][i]:
                check = False
            tmp += matrix[j][i]
    if check and tmp == size * size:
        p += 1
    elif check and tmp == 0:
        z += 1
    elif check and tmp == -(size * size):
        m += 1
    else:
        cut = size // 3
        nineRecur(sx,sy,cut)
        nineRecur(sx + cut,sy,cut)
        nineRecur(sx + 2 * cut,sy,cut)
        nineRecur(sx,sy + cut,cut)
        nineRecur(sx,sy + 2 * cut,cut)
        nineRecur(sx + cut,sy + cut,cut)
        nineRecur(sx + cut,sy + 2 * cut,cut)
        nineRecur(sx + 2 * cut,sy + cut,cut)
        nineRecur(sx + 2 * cut,sy + 2 * cut,cut)

nineRecur(0,0,n)
print(m)
print(z)
print(p)