import sys
input = sys.stdin.readline

n = int(input().split())
aset = set([])
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "add":
        aset.add(cmd[1])
    elif cmd[0] == "remove":
        print("a")