#BOJ 15651 - N과 M(3)
n,m = map(int,input().split())
s = []

def printm():
    if len(s) == m:
        print(' '.join(list(map(str,s))))
        return
    
    else:
        for i in range(1,n+1):
            s.append(i)
            printm()
            s.pop()
printm()