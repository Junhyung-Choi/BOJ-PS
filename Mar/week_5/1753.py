#BOJ 1753 - 최단경로
import sys
import heapq

input = sys.stdin.readline
INF = 123456789

nodesize,linksize = map(int,input().split())
startnode = int(input())

heap = []
weight = [INF] * (nodesize + 1)
matrix = [[] for _ in range(nodesize + 1)]

for _ in range(linksize):
    u,v,w = map(int,input().split())
    matrix[u].append((w,v))

def dijkstra():
    global startnode
    weight[startnode] = 0
    heapq.heappush(heap,(0,startnode))
    while heap:
        curweight,curnode = heapq.heappop(heap)
        if weight[curnode] < curweight:
            continue
        for goingweight, nextnode in matrix[curnode]:
            nextweight = curweight + goingweight
            if nextweight < weight[nextnode]:
                weight[nextnode] = nextweight
                heapq.heappush(heap,(nextweight,nextnode))

dijkstra()

for i in range(1,nodesize + 1):
    if weight[i] == INF:
        print("INF")
    else:
        print(weight[i])