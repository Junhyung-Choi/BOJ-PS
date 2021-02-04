import sys
input = sys.stdin.readline
n,m = map(int,input().split())
narr = set()
marr = set()
for _ in range(n):
    narr.add(input().rstrip())
for _ in range(m):
    marr.add(input().rstrip())
cross = sorted(list(narr.intersection(marr)))
print(len(cross))
for i in cross:
    print(i)
