import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

queue = []
pcnum = int(input())
conpcnum = int(input())
conarr = [[] for i in range(pcnum+1)]
dcheck = [False] * (pcnum + 1)
bcheck = []
cnt = 0

for _ in range(conpcnum):
    i,j = map(int,input().split())
    conarr[i].append(j)
    conarr[j].append(i)

def dfs(dot):
    global cnt
    if dcheck[dot] == False:
        dcheck[dot] = True
        cnt += 1
    for i in range(len(conarr[dot])):
        if dcheck[conarr[dot][i]] == False:
            dfs(conarr[dot][i])

def bfs(start):
    bcheck.append(start)
    queue.append(start)
    while queue != []:
        tmp = queue.pop(0)
        for i in conarr[tmp]:
            if i not in bcheck:
                bcheck.append(i)
                queue.append(i)

#Choose DFS or BFS
#dfs(1)
bfs(1)
print(cnt-1)