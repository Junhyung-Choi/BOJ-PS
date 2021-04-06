#BOJ 2740 - 행렬 곱셈
import sys
input = sys.stdin.readline

matA = []
matB = []

n,m = map(int,input().split()) 

for _ in range(n):
    matA.append(list(map(int,input().split())))

m,k = map(int,input().split())

for _ in range(m):
    matB.append(list(map(int,input().split())))

powmat = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for a in range(m):
            powmat[i][j] += matA[i][a] * matB[a][j]

for i in range(n):
    for j in range(k):
        print(powmat[i][j], end = " ")
    print() 
