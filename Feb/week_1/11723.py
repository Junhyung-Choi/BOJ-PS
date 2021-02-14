import sys
input = sys.stdin.readline

n = int(input())
aset = set([])
def add(num):
    aset.add(num)

def remove(num):
    aset.discard(num)

def toggle(num):
    if num in aset:
        aset.remove(num)
    else:
        aset.add(num)

def check(num):
    if num in aset:
        print(1)
    else:
        print(0)

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "add":
        add(cmd[1])
    elif cmd[0] == "remove":
        remove(cmd[1])
    elif cmd[0] == "check":
        check(cmd[1])
    elif cmd[0] == "toggle":
        toggle(cmd[1])
    elif cmd[0] == "all":
        aset.update(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif cmd[0] == "empty":
        aset.clear()
        