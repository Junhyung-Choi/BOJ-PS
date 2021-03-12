#BOJ 1010 - 다리놓기
import sys,math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    west,east = map(int,input().split())
    print((math.factorial(east) // (math.factorial(west) * math.factorial(east-west))))