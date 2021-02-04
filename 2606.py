import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

pcnum = int(input())
conpcnum = int(input())
conarr = [[] for i in range(pcnum+1)]
check = [False] * (pcnum + 1)
cnt = 0

for _ in range(conpcnum):
    i,j = map(int,input().split())
    conarr[i].append(j)
    conarr[j].append(i)

def dfs(dot):
    global cnt
    if check[dot] == False:
        check[dot] = True
        cnt += 1
    for i in range(len(conarr[dot])):
        if check[conarr[dot][i]] == False:
            dfs(conarr[dot][i])
dfs(1)
print(cnt-1)