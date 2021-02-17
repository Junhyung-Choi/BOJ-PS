#BOJ 11286 - 절댓값 힙
import sys
import heapq
input = sys.stdin.readline

heap = []

N = int(input())

for _ in range(N):
    node = int(input())
    if node == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    elif node <0:
        heapq.heappush(heap,(-node,node))
    else:
        heapq.heappush(heap,(node,node))
