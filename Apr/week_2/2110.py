#BOJ 2110 - 공유기 설치
import sys
input = sys.stdin.readline

housenum,share = map(int,input().split())

house = []

for _ in range(housenum):
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start+end) // 2 
    tmp = house[0]
    cnt = 1
    
    for i in range(1, len(house)):
        if tmp+mid <= house[i]: # gap 이상
            cnt += 1
            tmp = house[i]
    if share <= cnt:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)