import sys
input = sys.stdin.readline
queue = []
pcnum = int(input())
conpcnum = int(input())
conarr = [[] for i in range(pcnum+1)]
check = []

for _ in range(conpcnum):
    i,j = map(int,input().split())
    conarr[i].append(j)
    conarr[j].append(i)

def bfs(start):
    check.append(start)
    queue.append(start)
    while queue != []:
        tmp = queue.pop(0)
        for i in conarr[tmp]:
            if i not in check:
                check.append(i)
                queue.append(i)
bfs(1)
print(len(check)-1)