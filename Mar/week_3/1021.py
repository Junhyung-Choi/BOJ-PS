#BOJ 1021 - 회전하는 큐
from collections import deque
qsize, popnum = map(int,input().split())
poplist = list(map(int,input().split()))
data = deque()
for num in range(1,qsize + 1):
    data.append(num)

def shorter(key):
    pos = data.index(key)
    if pos < len(data) - pos: #if key is closer at front than back, return True // else : return False
        return True, pos
    else:
        return False,len(data) - pos
sum = 0
for index in range(popnum):
    left,count = shorter(poplist[index])
    sum += count
    for _ in range(count):
        if left:
            data.append(data.popleft())
        else:
            data.appendleft(data.pop())
    data.popleft()
print(sum)