#BOJ 1676 - 팩토리얼 0의 개수
import math
n = 1
while n != 0:
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        if i % 125 == 0:
            sum += 3
        elif i % 25 == 0 :
            sum += 2
        elif i % 5 == 0:
            sum += 1
    print(sum)
