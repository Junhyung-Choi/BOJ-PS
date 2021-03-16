#BOJ 15654 - N과 M(5)
import sys
input = sys.stdin.readline

listsize, combsize = list(map(int,input().split()))
numlist = sorted(list(map(int,input().split())))

comblist = []
def makeComb(size):
    if size == combsize:
        for node in comblist:
            print(node,end = " ")
        print()
        return
    else:
        for index in range(listsize):
            if numlist[index] not in comblist:
                comblist.append(numlist[index])
                makeComb(size + 1)
                comblist.pop()
makeComb(0)