# 다음과 같이 import를 사용할 수 있습니다.
# import math
from collections import deque

def solution(garden):
    queue = deque()
    gardensize = len(garden)
    timemat = [[0] * gardensize for _ in range(gardensize)]
    for i in range(gardensize):
        for j in range(gardensize):
            if garden[i][j] == 1:
                queue.append((i,j))
    while queue:
        blmx,blmy = queue.popleft()
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx = blmx + dx
            ny = blmy + dy
            if 0 <= nx < gardensize and 0 <= ny < gardensize and garden[nx][ny] == 0:
                garden[nx][ny] = 1
                timemat[nx][ny] = timemat[blmx][blmy] + 1
                queue.append((nx,ny))
    answer = -1
    for i in range(gardensize):
        for j in range(gardensize):
            if timemat[i][j] > answer:
                answer = timemat[i][j]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")