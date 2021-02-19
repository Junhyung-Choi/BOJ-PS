#BOJ 15686 - 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

SIZE,MAX_STORE = map(int,input().split())
city = []
chick = []
houses = []

for row in range(SIZE):
    city.append(list(map(int,input().split())))

for row in range(SIZE):
    for area in range(SIZE):
        if city[row][area] == 2:
            chick.append((row,area))
        if city[row][area] == 1:
            houses.append((row,area))
"""
def comb(lst,n):
    result = []
    if n > len(lst):
        return result
    if n == 1:
        for i in lst:
            result.append(i)
    elif n > 1:
        for i in range(len(lst)-n+1):
            for tmp in comb(lst[i+1:],n-1):
                result.append(lst[i])
                result.append(tmp)
    return result
"""
chicken_distance = 123456789
#print(comb(chick,MAX_STORE))
#print(list(combinations(chick,MAX_STORE)))

for stores in list(combinations(chick,MAX_STORE)):    
    sum = 0
    for house in houses:
        mrange = 123456789
        for c in stores:
            d = abs(c[0]-house[0]) + abs(c[1] - house[1])
            mrange = min(mrange,d)
        sum += mrange
    chicken_distance = min(sum,chicken_distance)

print(chicken_distance)
