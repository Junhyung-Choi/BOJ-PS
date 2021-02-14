#BOJ 1697 - 숨바꼭질
from collections import deque

spos,bpos = map(int,input().split())
queue = deque()
time = [0] * 100001

queue.append(spos)
while queue:
    curpos = queue.popleft()
    if curpos == bpos:
        print(time[curpos])
        break
    for nextpos in [curpos - 1,curpos + 1,curpos * 2]:
        if nextpos > -1 and nextpos < 100001 and time[nextpos] == 0:
            queue.append(nextpos)
            time[nextpos] = time[curpos] + 1
