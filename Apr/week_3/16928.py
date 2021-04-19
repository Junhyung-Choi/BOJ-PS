#BOJ 16928 - 뱀과 사다리 게임

#1,100 must not be startpoint and endpoint
import sys
from collections import deque

input = sys.stdin.readline

ladders = {}
snakes = {}

ladder,snake = map(int,input().split())

board = list(range(101)) 
visited = [-1] * 101

#ladder : start, end(start < end) //getting higher 
for index in range(ladder):
    start,end = map(int,input().split())
    ladders[start] = end

#snake : start, end(start > end) //getting lower
for index in range(snake):
    start,end = map(int,input().split())
    snakes[start] = end

d = [1,2,3,4,5,6]
queue = deque()

def bfs():
    startpoint = 1
    endpoint = 100
    queue.append(startpoint)
    visited[startpoint] = 0
    while queue:
        curpos = queue.popleft()
        if curpos == endpoint: 
            return visited[curpos]
        for i in range(6): 
            nextpos = curpos + d[i]
            if nextpos > 100:
                continue
            if nextpos in ladders.keys():
                nextpos = ladders[nextpos]
            if nextpos in snakes.keys():
                nextpos = snakes[nextpos]
            if visited[nextpos] == -1:
                visited[nextpos] = visited[curpos] + 1
                queue.append(nextpos)

print(bfs())