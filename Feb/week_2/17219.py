#BOJ 17219 - 비밀번호 찾기
import sys
input = sys.stdin.readline 

m,n = map(int,input().split())
d = {}
for _ in range(m):
    address,password = input().split()
    d[address] = password
for _ in range(n):
    address = input().rstrip()
    print(d[address])
