# 3월 1주차 문제해설
- [1904 - 01타일](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/1904.py "1904 - 01타일")
- [1912 - 연속 합](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/1912.py "1912 - 연속 합")
- [2156 - 포도주 시식](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/2156.py "2156 - 포도주 시식")
- [9184 - 신나는 함수 실행](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/9184.py "9184 - 신나는 함수 실행")
- [10844 - 쉬운 계단 수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/10844.py "10844 - 쉬운 계단 수")
- [11053 - 가장 긴 증가하는 부분 수열](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/11053.py "11053 - 가장 긴 증가하는 부분 수열")
- [14888 - 연산자 끼워넣기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/14888.py "14888 - 연산자 끼워넣기")
- [14889 - 스타트와 링크](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/14889.py "14889 - 스타트와 링크")
---
해설 없는 문제

---
## [1904 - 01타일](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/1904.py "1904 - 01타일")
- 시간제한 : 0.75초 | 메모리제한 : 256MB

N에 따른 가짓수를 나열해보면 피보나치수열을 따른다는 것을 알 수 있다. DP를 활용해서 문제를 풀면 된다.

> 왜 피보나치 수열을 따르는가? 
> 00이 붙어서 나올 수 밖에 없기 때문에 n-1개의 가짓수 끝에 1을 붙이는 것(n-1) + 2개를 뺀 가짓수 끝에 00을 붙이는 것(n-2)개의 가짓수를 더할 수 밖에 없기 때문이다.
>> n == 3의 경우 001(n=2 끝에 1붙이기),100(n=1끝에 00붙이기),111(n=2끝에 1붙이기)
>>> n == 4의 경우 0000(n=2끝에 00붙이기),1001(n==3 끝에 1붙이기),0011(n==3끝에 1붙이기),1100(n=2끝에 00붙이기),1111(n=3끝에 1붙이기)  

|N      | 1        | 2        | 3        | 4        | 5        | 6        | ...     |
|:-----:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|가짓수 |  1개     |  2개     |  3개     |  5개     |  8개     |  13개     |  ...     |
  
---
## [1912 - 연속 합](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/1912.py "1912 - 연속 합")
- 시간제한 : 1초 | 메모리제한 : 128MB
본인까지 연속적으로 이루어진 합보다 본인의 수가 더 크다면 본인부터 다시 연속합을 실시하는게 더 큰 연속합을 만들 수 있다는 의미이다.
이를 코드로 보이자면 아래와 같다.
모든 수에 대해 아래 코드를 반복문으로 돌리고, 그중 가장 큰 값을 구하면 정답을 찾을 수 있다.

```python
dp[i] = max(dp[i-1] + data[i], data[i])
```
---
## [2156 - 포도주 시식](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/2156.py "2156 - 포도주 시식")
- 시간제한 : 2초 | 메모리제한 : 128MB

*주의! 아래 설명에선 `dp`는 0번째 값이 0이고, `data`는 0번째부터 유의미한 데이터가 들어간다는 가정하에 진행된다.

문제 조건중 2번째 규칙
> 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

를 주의깊게 보아야한다.

이 말은 2잔을 마시고 한잔 혹은 두잔을 마시지 않고 다음 잔을 넘겨야 한다는 의미이다.

* 세잔째 안마시면 가운데 있는 포도주를 안마신다는 의미이므로 최대한 많이 마실수 있는 경우가 아니다.

n번째 잔을 무조건 마신다고 가정했을때의 최댓값 배열을 `dp`라고 하자.

첫번째 잔을 마신다고 했을때 최댓값은 첫번째 잔의 값이다.

두번째 잔을 마신다고 했을때의 최댓값은 첫번째, 두번째 잔의 합이다.

세번째 잔부턴 3잔 연속으로 못마시므로 첫번째 잔을 마실 것인지, 두번째 잔을 마실 것인지 골라야 한다. 

`dp[3] = max(dp[3-1],dp[3-2]) + data[3-1]`

네번째 잔부턴 두번 연속 안 마실 경우를 고려해야하므로 아래와 같은 점화식을 사용해야한다.
`dp[n] = max(dp[n-2],dp[n-3] + data[n-2], dp[n-4]+data[n-2]) + data[n-1]`


### * 풀이 2번째 버전 
n번까지의 잔만 있다고 가정했을때 최댓값들을 모아둔 배열을 dp라고 하자

n번째 잔을 마신다고 했을때의 점화식은
`dp[n] = max(dp[n-3] + data[n-1], dp[n-2]) + data[n-1]` 이라고 표현할 수 있다.

그러나 3잔을 연속으로 마실수 없다는 조건에 따라, n번째 잔을 마실 경우 사이에 있는 더 많은 양이 담긴 와인잔을 못마시는 경우가 생긴다.

그러므로 n번째 잔을 마시지 않았을 경우의 최댓값과 비교해, 그중 더 많이 마실수 있는 양을 dp에 배정해야 한다.

이는 곧 `dp[n] = max(dp[n],dp[n-1])`의 점화식을 한번 더 실행해주면 된다는 의미이다.

코드
```python
#BOJ 2156 - 포도주 시식
import sys
input = sys.stdin.readline
arr = []
n = int(input())
dp = [0] * (n+1)

for _ in range(n):
    arr.append(int(input()))
dp[1] = arr[0]
if n > 1:
    dp[2] = arr[0] + arr[1]
for i in range(3,n+1):
    dp[i] = max(dp[i-3] + arr[i-2], dp[i-2]) + arr[i-1]
    dp[i] = max(dp[i-1],dp[i])
print(max(dp))
```

---
## [9184 - 신나는 함수 실행](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/9184.py "9184 - 신나는 함수 실행")
- 시간제한 : 1초 | 메모리제한 : 128MB

문제에 주어진 점화식을 그대로 구현하되, 3차원 배열을 구현해서 기존에 계산되었던 값이면 그 값을 사용하는 방식으로 구현하면 된다.

```python
def w(a,b,c):
    ...
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    ...
```
---
## [10844 - 쉬운 계단 수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/10844.py "10844 - 쉬운 계단 수")
- 시간제한 : 1초 | 메모리제한 : 256MB

길이가 n이며 0~9까지 끝나는 숫자의 수를 data[n] 에 배열로 저장한다고 치자.
0으로 끝나는 수는 길이가 n-1인 수에서 1로 끝나는 수만 0으로 끝날 수 있으므로 `data[n-1][1]`을 사용하면 된다.
마찬가지로 9로 끝나는 수 또한 `data[n-1][8]`이라 표현할 수 있다.
그리하여 사이에 있는 수는 `data[n-1][i-1] + data[n-1][i+1]`임을 알 수 있다.
정답은 1,000,000,000으로 나누어야 한다는 것을 유의해서 풀자

```python
data[1] = [0,1,1,1,1,1,1,1,1,1]
data[2] = [1,1,2,2,2,2,2,2,2,1]
...
```


---
## [11053 - 가장 긴 증가하는 부분 수열](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/11053.py "11053 - 가장 긴 증가하는 부분 수열")
- 시간제한 : 1초 | 메모리제한 : 256MB

본인보다 작은 모든 수에 대해서 그 수의 dp값 + 1보다 본인의 dp값이 작다면 갱신해주고, 본인값이 크다면 유지하면 된다. 이를 1부터 n까지 진행, dp의 최댓값을 출력해주면 된다.

---
## [14888 - 연산자 끼워넣기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/14888.py "14888 - 연산자 끼워넣기")
- 시간제한 : 2초 | 메모리제한 : 512MB
모든 연산자를 한개씩 써보는 형식으로 진행하면 되는데, `index`와 `operlist(남은 연산자의 리스트)`를 `doCal()`로 백트래킹 해서 풀면 된다.

------
## [14889 - 스타트와 링크](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_1/14889.py "14888 - 스타트와 링크")
- 시간제한 : 2초 | 메모리제한 : 512MB

백트래킹 기법을 사용해서 풀면 된다. 절반의 개수만큼 `start`에 고르게 된다면 나머지 사람을 `link`에 넣고 `getAbility()`함수를 통해 스타트의 합과 링크의 합을 구하고 이의 차이값의 최솟값을 매번 갱신해주면 결과를 알 수 있다.

그러나 a,b,c,d 중 스타트에 a,b 링크에 c,d를 고르는 차이값은 링크에 a,b 스타트에 c,d 를 고르는 것과 같으므로 `maxComb`로 n개중 절반을 고르는 조합의 수의 절반을 계산해, `cnt`가 이를 넘기면 모든 경우의 수를 판독했다고 보고 함수를 종료시키면 시간을 단축할 수 있다.

---