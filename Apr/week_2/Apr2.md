# 4월 2주차 문제해설
[13172 - Σ](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_2/13172.py "13172 - Σ")
[2110 - 공유기 설치](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_2/2110.py "2110 - 공유기 설치")
[11659 - 구간 합 구하기 4](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_2/11659.py "11659 - 구간 합 구하기 4")
[14501 - 퇴사](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_2/14501.py "14501 - 퇴사")

---
해설 없는 문제

---
## [13172 - Σ](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_2/13172.py "13172 - Σ")
- 시간제한 : 0.5초 | 메모리제한 : 128MB

처음엔 문제를 잘 이해를 못했다.
결국은 모든 주사위 기댓값들을 기약분수 형태로 나타내고 b의 모듈러 곱셈에 대한 역원을 구하고 더하면 된다고 한다. X가 충분히 크므로 (b^x-2)%x = b^(-1)으로 볼 수 있다.
여기서 X가 매우 크므로 분할 정복에 의한 거듭제곱법을 사용해야 함에 주의한다.

```python
#분할정복에 의한 거듭제곱법 알고리즘
def bigSqaure(num,sqnum):
    if sqnum == 1:
        return num
    if sqnum % 2 == 1:
        return num * bigSqaure(num,sqnum - 1) % mod
    half = bigSqaure(num,sqnum // 2)
    return (half * half) % mod
```

```python
for _ in range(dicenum):
    side, poly = map(int,input().split())
    #기약분수
    gnum = math.gcd(side,poly)
    side = side // gnum
    poly = poly // gnum
    #역원 구하고 더하기
    yuk = bigSqaure(side,mod-2)
    result += (poly * yuk)
    result = result % mod
```

---
## [2110 - 공유기 설치](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_2/2110.py "2110 - 공유기 설치")
- 시간제한 : 2초 | 메모리제한 : 128MB

이분탐색 문제이다.
일정 간격을 기준으로 공유기를 설치해보고, 만약 더 설치해야한다면 간격을 줄이고, 공유기를 줄여야 한다면 간격을 늘리면 된다.

---
## [11659 - 구간 합 구하기 4](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_2/11659.py "11659 - 구간 합 구하기 4")
- 시간제한 : 2초 | 메모리제한 : 128MB

미리 처음부터 끝까지 차례대로 구간의 합을 구해두고, 원하는 구간을 입력받아서 구간합끼리 빼주면 원하는 구간의 합을 구할 수 있다.

---
## [14501 - 퇴사](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_2/14501.py "14501 - 퇴사")
- 시간제한 : 1초 | 메모리제한 : 128MB

일단 dp에 모든 수익을 그 날짜의 수익으로 해두고 2번째날부터 마지막날까지 반복문을 돌린다.
반복문 안쪽에선 첫날부터 본인 날짜 직전까지 시간과 가격이 맞는 상황에서 dp보다 높은 수익을 올릴 수 있다면 dp를 수정해주고 마지막에 dp중 가장 크면서 시간을 지킬 수 있는 것을 뽑아내면 된다.

---
