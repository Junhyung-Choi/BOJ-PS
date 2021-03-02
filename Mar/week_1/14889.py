#BOJ 14889 - 스타트와 링크
import sys
import math
input = sys.stdin.readline

num = int(input())
half = num // 2 
matrix = []
maxComb = math.factorial(num) // ((math.factorial(half) ** 2) * 2)
#print(maxComb)
for _ in range(num):
    matrix.append(list(map(int,input().split())))

start = []
minor = 12345678910
cnt = 0

def getAbility(link):
    # print(start,link)
    ssum = 0
    lsum = 0
    for x in range(half-1):
        for y in range(x+1,half):
            # print(start[x-1],start[y-1],link[x-1],link[y-1])
            ssum += matrix[start[x]-1][start[y]-1] + matrix[start[y]-1][start[x]-1]
            lsum += matrix[link[x]-1][link[y]-1] + matrix[link[y]-1][link[x]-1]
    return ssum,lsum

def getMinor(snum):
    global minor,num,cnt
    if maxComb <= cnt:
        return
    if len(start) == half:
        link = []
        for i in range(1,num+1):
            if i not in start:
                link.append(i)
        ssum,lsum = getAbility(link)
        minor = min(minor,abs(ssum - lsum))
        cnt += 1
        return
    else:
        for index in range(snum,num+1):
            # if index in start:
            #     continue
            # if start and index < start[0]:
            #     continue
            start.append(index)
            # print(start,snum)
            getMinor(index + 1)
            start.pop()

getMinor(1)
print(minor)