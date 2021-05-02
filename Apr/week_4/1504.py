#BOJ 1504 - 특정한 최단 경로
import sys
import heapq
input = sys.stdin.readline

node,line = map(int,input().split())
matrix = [[] for _ in range(node+1)]

for _ in range(line):
    node_first, node_second, distance = map(int,input().split())
    matrix[node_first].append([node_second,distance])
    matrix[node_second].append([node_first,distance])

must_first, must_second = map(int,input().split())

def dijkstra(start):
    dp = [123456789 for i in range(node+1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap,[0,start])
    while heap:
        current_distance,current_node = heapq.heappop(heap)
        for next_node,next_distance in matrix[current_node]:
            total_distance = next_distance + current_distance
            if dp[next_node] > total_distance:
                dp[next_node] = total_distance
                heapq.heappush(heap,[total_distance,next_node])
    return dp

origin = dijkstra(1)
must_first_dp = dijkstra(must_first)
must_second_dp = dijkstra(must_second)
result = min(origin[must_first] + must_first_dp[must_second] + must_second_dp[node], origin[must_second] + must_second_dp[must_first] + must_first_dp[node])

if result >= 123456789:
    print(-1)
else:
    print(result)