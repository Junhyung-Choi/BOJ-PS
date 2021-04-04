#BOJ 12851 - 숨바꼭질 2
from collections import deque

spos,bpos = map(int,input().split())
queue = deque()
time = [-1] * 100001
time[spos] = 0
queue.append(spos)
cnt = 0
while queue:
    curpos = queue.popleft()
    if curpos == bpos:
        cnt += 1
    for nextpos in [curpos - 1,curpos + 1,curpos * 2]:
        if nextpos > -1 and nextpos < 100001 and (time[nextpos] == -1 or time[nextpos] >= time[curpos] + 1):
            queue.append(nextpos)
            time[nextpos] = time[curpos] + 1

print(time[bpos])
print(cnt)