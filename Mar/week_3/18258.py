#BOJ 18258 - 큐2
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
queue = deque()
for test_case in range(T):
    cmd = list(input().split())
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if not queue:
            print("-1")
        else:
            print(queue.popleft())
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if not queue:
            print("-1")
        else:
            print(queue[0])
    elif cmd[0] == "back":
        if not queue:
            print("-1")
        else:
            print(queue[len(queue)-1])