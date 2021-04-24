#BOJ 1865 - 웜홀
import sys
input = sys.stdin.readline

INF = 123456789

TC = int(input())
for test_case in range(TC):
    
    nodenum,roadnum,wormnum = map(int,input().split())
    
    distance = [123456789] * (nodenum + 1)
    matrix = [[] for _ in range(nodenum + 1)]

    for _ in range(roadnum):
        start,end,value = map(int,input().split())
        matrix[start].append((end,value))
        matrix[end].append((start,value))
    
    for _ in range(wormnum):
        start,end,value = map(int,input().split())
        matrix[start].append((end,-1 * value))

    distance[start] = 0

    for _ in range(1,nodenum):
        for node in range(1,nodenum+1):
            for neighbor,dist in matrix[node]:
                if distance[neighbor] > distance[node] + dist:
                    distance[neighbor] = distance[node] + dist
    
    isCycle = False
    for node in range(1,nodenum+1):
        for neighbor,dist in matrix[node]:
            if distance[neighbor] > distance[node] + dist:
                isCycle = True
    if isCycle:
        print("YES")
    else:
        print("NO")