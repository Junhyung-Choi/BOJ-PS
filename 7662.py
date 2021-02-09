#BOJ 7662 - 이중 우선순위 큐
import sys
import heapq
input = sys.stdin.readline
T = int(input())
def put(num,index):
    heapq.heappush(minHeap,(num,index))
    heapq.heappush(maxHeap,(-num,index))

def delete(cmd):
    if cmd == '1':
        while maxHeap and visited[maxHeap[0][1]]:
            heapq.heappop(maxHeap)
        if maxHeap:
            visited[maxHeap[0][1]] = True
            heapq.heappop(maxHeap)
    else:
        while minHeap and visited[minHeap[0][1]]:
            heapq.heappop(minHeap)
        if minHeap:
            visited[minHeap[0][1]] = True
            heapq.heappop(minHeap)

for test_case in range(T):
    minHeap = []
    maxHeap = []
    visited = [False] * 1000001
    C = int(input())
    index = 0
    for _ in range(C):
        cmd = input().split()
        if cmd[0] == "I":
            put(int(cmd[1]),index)
            index += 1
        else:
            delete(cmd[1])
    while minHeap and visited[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and visited[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    if minHeap and maxHeap:
        print(-maxHeap[0][0],minHeap[0][0])
    else:
        print("EMPTY")