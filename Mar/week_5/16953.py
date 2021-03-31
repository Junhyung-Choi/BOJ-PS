#BOJ 16953 - A -> B
from collections import deque
# A를 B로 바꾸려고 한다. 가능한 연산은
# 2곱하기
# 1을 수의 가장 오른쪽에 추가하기

start,end = map(int,input().split())
queue = deque()
queue.append(start)
cnt = 0
cntdic = {}
cntdic[start] = 0

while queue:
    tmp = queue.popleft()
    result = -1
    if tmp == end:
        result = cntdic[tmp] + 1
        break
    for next in [tmp * 2, tmp * 10 + 1]:
        if next <= end:
            queue.append(next)
            cntdic[next] = cntdic[tmp] + 1
print(result)