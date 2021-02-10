#BOJ 17626 - Four Squares
import math

n = int(input())
arr = [5] * 50001
arr[0] = 0
arr[1] = 1
for i in range(2,n+1):
    low = 5
    for j in range(i):
        if j ** 2 > i:
            break
        tmp = i - (j ** 2)
        low = min(low,arr[tmp])
    arr[i] = low + 1
print(arr[n])