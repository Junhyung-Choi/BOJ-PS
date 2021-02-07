#BOJ 1764 - 듣보잡
import sys
input = sys.stdin.readline

#ns : 보지도 못한 사람, nh : 듣지도 못한 사람
ns,nh = map(int,input().split())
nsset = set()
nhset = set()

for _ in range(ns):
    nsset.add(input().rstrip())

for _ in range(nh):
    nhset.add(input().rstrip())

interset = sorted(list(nsset.intersection(nhset)))
print(len(interset))

for i in interset:
    print(i)
