#BOJ 13305 - 주유소
cityNum = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

minprice = price[0]
length = 0
total = 0
for city in range(cityNum-1):
    if minprice > price[city]:
        total += (length * minprice)
        minprice = price[city]
        length = dist[city]
    else:
        length += dist[city] 
total += (length * minprice)
print(total)