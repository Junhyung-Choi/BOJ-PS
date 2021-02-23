#BOJ 1011 - Fly me to the Alpha Centauri
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    x,y = map(int,input().split())
    dist = y - x
    sig = [0,2]
    i = 1
    while dist > sig[i]:
        i += 1
        sig.append(sig[i-1] + i*2)
    #print(i)
    #print(sig)
    if dist <= ((sig[i] + sig[i-1]) // 2):
        print(i * 2 - 1)
    else:
        print(i * 2)