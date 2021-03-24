#BOJ 15663 - N과 M(9)
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
data = sorted(list(map(int,input().split())))

queue = deque()
check = [False] * n

def showComb(queue):
    for node in queue:
        print(node, end = " ")
    print()

def getComb(cnt):
    if cnt == m:
        showComb(queue)
        return
    last = 0
    for i in range(n):
        if not check[i] and data[i] != last:
            check[i] = True
            queue.append(data[i])
            last = data[i]
            getComb(cnt+1)
            check[i] = False
            queue.pop()

getComb(0)