#BOJ 15652 - N과 M(4)
n,m = map(int,input().split())
s = []

def printm(start):
    if len(s) == m:
        print(' '.join(list(map(str,s))))
        return
    
    else:
        for i in range(start,n+1):
            s.append(i)
            printm(i)
            s.pop()
printm(1)