#BOJ 9019 - DSLR
from collections import deque

T = int(input())

for test_case in range(T):
    origin,goal = map(int,input().split())
    queue = deque([("",origin)])
    visited = [0] * 10000
    visited[origin] = 1
    while queue:
        c,n = queue.popleft()
        if n == goal:
            print(c)
            break
        t = (n * 2) % 10000
        if visited[t] == 0:
            queue.append((c + "D",t))
            visited[t] = 1
        t = n - 1 if n != 0 else 9999
        if visited[t] == 0:
            queue.append((c + "S",t))
            visited[t] = 1
        t = n % 1000 * 10 + n // 1000    
        if visited[t] == 0:
            queue.append((c + "L",t))
            visited[t] = 1
        t = n % 10 * 1000 + n // 10       
        if visited[t] == 0:
            queue.append((c + "R",t))
            visited[t] = 1