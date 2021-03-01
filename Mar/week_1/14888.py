#BOJ 14888 - 연산자 끼워넣기

num = int(input())
numlist = list(map(int,input().split()))
operlist = list(map(int,input().split())) #[+, -, *, /]

max_result = -123456789
min_result = 123456789

def doCal(result,index,operlst):
    global num,max_result,min_result
    if index == num:
        max_result = max(max_result,result)
        min_result = min(min_result,result)
        return
    else:
        if operlst[0] != 0:
            doCal(result + numlist[index],index + 1,[operlst[0]-1,operlst[1],operlst[2],operlst[3]])
        if operlst[1] != 0:
            doCal(result - numlist[index],index + 1,[operlst[0],operlst[1]-1,operlst[2],operlst[3]])
        if operlst[2] != 0:
            doCal(result * numlist[index],index + 1,[operlst[0],operlst[1],operlst[2]-1,operlst[3]])
        if operlst[3] != 0:
            doCal(int(result/numlist[index]),index + 1,[operlst[0],operlst[1],operlst[2],operlst[3]-1])

doCal(numlist[0],1,operlist)
print(max_result)
print(min_result)