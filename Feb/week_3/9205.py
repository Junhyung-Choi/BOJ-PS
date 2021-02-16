#BOJ 9205 - 맥주 마시면서 걸어가기

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(home,stores,end):
    queue = deque()
    visited = []
    queue.append(home)
    visited.append(home)
    while queue:
        tmp = queue.popleft()
        if tmp == end:
            print("happy")
            return 0
        for store in stores:
            distance = abs(tmp[0] - store[0]) + abs(tmp[1] - store[1])
            if store not in visited and distance <= 1000:
                queue.append(store)
                visited.append(store)
    print("sad")

for test_case in range(T):
    S = int(input())
    home = tuple(map(int,input().split()))
    stores = []
    for store in range(S):
        stores.append(tuple(map(int,input().split())))
    rock = tuple(map(int,input().split()))
    stores.append(rock)
    bfs(home,stores,rock)