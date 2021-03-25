#BOJ 15666 - N과 M(12)
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
data = sorted(list(set(map(int,input().split()))))

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
    for i in range(len(data)):
        if not queue or data[i] >= queue[cnt-1]:
            queue.append(data[i])
            getComb(cnt+1)
            queue.pop()

getComb(0)