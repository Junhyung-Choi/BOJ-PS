#BOJ 13549 - 숨바꼭질 3
from collections import deque

spos,bpos = map(int,input().split())
queue = deque()
time = [-1] * 100001
time[spos] = 0
queue.append(spos)
while queue:
    curpos = queue.popleft()
    if curpos == bpos:
        print(time[curpos])
        break
    for nextpos in [curpos - 1,curpos + 1,curpos * 2]:
        if nextpos > -1 and nextpos < 100001 and time[nextpos] == -1:
            if nextpos == curpos * 2:
                time[nextpos] = time[curpos]
                queue.appendleft(nextpos)
            else:
                time[nextpos] = time[curpos] + 1
                queue.append(nextpos)
