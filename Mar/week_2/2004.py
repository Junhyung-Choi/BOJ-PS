#BOJ 2004 - 조합 0의 개수
n,r = map(int,input().split())

def getZero(a):
    two,five = 0,0
    i = 2
    while i <= a:
        two += a // i
        i *= 2
    i = 5
    while i <= a:
        five += a // i
        i *= 5
    return two,five

nt,nf = getZero(n)
rt,rf = getZero(r)
nrt,nrf = getZero(n-r)
print(min(nt-rt-nrt,nf-rf-nrf))