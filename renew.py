"""
Markdown Renewing Program v.0.0.1
todo:
- (Tech) Reading README.md [o]
- (Tech) Getting File list [o]
- (Tech) Parsing README.md [o]
- (Function) Modifying README.md [o]
- (Function) Make Weekly PS Document [ ]
"""
import os

docProblems = [[[] for __ in range(5)] for _ in range(12)]
realProblems = [[[] for __ in range(5)] for _ in range(12)]
notin = []
doclastmonth, doclastweek = 1,0

month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
week = ["week_1","week_2","week_3","week_4","week_5"]

kordic = {"1월" : "Jan" , "2월" : "Feb" , "3월" : "Mar" , "4월" : "Apr" , "5월" : "May" , "6월" : "Jun" ,\
          "7월" : "Jul" , "8월" : "Aug" , "9월" : "Sep" , "10월" : "Oct" , "11월" : "Nov" , "12월" : "Dec",\
          "1주차" : "week_1" , "2주차" : "week_2" , "3주차" : "week_3" , "4주차" : "week_4" , "5주차" : "week_5"}\

numdic = {"Jan" : 0 , "Feb" : 1 , "Mar" : 2 , "Apr" : 3 , "May" : 4 , "Jun" : 5,\
          "Jul" : 6 , "Aug" : 7 , "Sep" : 8 , "Oct" : 9 , "Nov" : 10 , "Dec" : 11,\
          "week_1" : 0 , "week_2" : 1 , "week_3" : 2 , "week_4" : 3 , "week_5" : 4}

def getDocsProblems():
    global doclastmonth,doclastweek
    f = open("README.md",'r')
    cnt = 1
    add = False
    m = 1
    w = 0
    while True:
        line = f.readline()
        if not line : break
        # print(str(cnt) + ": " + line,end = '')
        if line[0:3] == "---":
            add = False
        if add and line != "\n":
            docProblems[m][w].append(line[1:6].rstrip() + ".py")
        if cnt > 10 and line[0:2] == "##":
            if line[5].isdecimal():
                m = int(line[4:6]) - 1
            else:
                m = int(line[4]) - 1
            w = int(line[7]) - 1
            add = True
        cnt += 1
    doclastmonth = m
    doclastweek = w
    # for w in result:
    #     print(w)
    # print(" ")
    
    f.close()

def getRealProblems():
    for mon in month:
        for wk in week:
            try:
                wd = proj + "/" + mon + "/" + wk
                os.chdir(wd)
                # print("At: ",os.getcwd())
                realProblems[numdic[mon]][numdic[wk]] += os.listdir(os.getcwd())
            except FileNotFoundError:
                continue

def showProblems(problems):
    for week in problems:
        print(week)

def compareProblems():
    for midx in range(12):
        for widx in range(5):
            for prob in realProblems[midx][widx]:
                if prob not in docProblems[midx][widx] and prob[0].isdecimal():
                    notin.append((prob,midx,widx))

print("Current Working Directory :",os.getcwd())
proj = os.getcwd()
getDocsProblems()
getRealProblems()
compareProblems()
os.chdir(proj)
print(notin)
doc = open("README.md","a")

for nproblem in notin:
    number, midx, widx = nproblem
    os.chdir(proj + "/" + month[midx] + "/" + week[widx])
    f = open(number,"r")
    name = (f.readline().rstrip())[12:].lstrip()
    f.close()
    print(doclastmonth,midx,doclastweek,widx)
    if doclastmonth < midx or doclastweek < widx:
        doc.write("\n")
        doc.write("---\n")
        title =  "## [" + str(midx+1) + "월 " + str(widx+1) + "주차](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/" + \
        month[midx] + "/" + week[widx] + "/" + month[midx] + str(widx+1) + ".md " + " \"" + str(midx + 1) + "월 " + str(widx + 1) + "주차\")"
        doc.write(title + "\n")
        doc.write("\n")
        doclastmonth,doclastweek = midx, widx
    sentence = ("["+number + " - " + name + "](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/" + \
                   month[midx] + "/" + week[widx] + "/" + number + " \"" + number.split(".")[0] + " - " + name + "\") | ")
    print(sentence)
    doc.write(sentence + "\n")
doc.close()

last = os.getcwd()

os.chdir(proj)

