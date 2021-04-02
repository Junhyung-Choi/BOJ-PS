#BOJ 1916 - 최소비용 구하기
import sys, heapq
input = sys.stdin.readline

INF = 123456789

citynum = int(input())
busnum = int(input())

matrix = [[] for _ in range(citynum + 1)]
cost = [INF] * (citynum + 1)
heap = []

for _ in range(busnum):
    startcity, endcity, buscost = map(int,input().split())
    matrix[startcity].append((buscost,endcity))

def dijkstra(start):
    cost[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        nodecost,node = heapq.heappop(heap)
        if cost[node] < nodecost:
            continue
        for buscost, goalcity in matrix[node]:
            mincost = nodecost + buscost
            if mincost < cost[goalcity]:
                cost[goalcity] = mincost
                heapq.heappush(heap,(mincost,goalcity))

s,e = map(int,input().split())

dijkstra(s)

print(cost[e])