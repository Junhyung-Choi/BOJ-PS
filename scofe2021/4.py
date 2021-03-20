#Scofe 4 - 안 본 콘텐츠 없게 해주세요
import sys
input = sys.stdin.readline
genre = list(map(float,input().split()))
genredic = {}
genredic["A"] = genre[0]
genredic["B"] = genre[1]
genredic["C"] = genre[2]
genredic["D"] = genre[3]
genredic["E"] = genre[4]
xsize,ysize = map(int,input().split())
contents = [[[] for __ in range(ysize)] for _ in range(xsize)]
for x in range(xsize):
    condata = input()
    for y in range(ysize):
        contents[x][y].append(condata[y])
for x in range(xsize):
    condata = input()
    for y in range(ysize):
        contents[x][y].append(condata[y])

result = []
tmp = []
for x in range(xsize):
    for y in range(ysize):
        if contents[x][y][0] == "Y":
            tmp.append([contents[x][y], x,y])
tmp.sort(key = lambda x: genredic[x[0][1]] * -1)
result += tmp
tmp = []
for x in range(xsize):
    for y in range(ysize):
        if contents[x][y][0] == "O":
            tmp.append([contents[x][y], x,y])
tmp.sort(key = lambda x: genredic[x[0][1]] * -1)
result+=tmp
for con in result:
    print(con[0][1]+" "+str(genredic[con[0][1]])+" "+str(con[1])+" "+str(con[2]))