# 3월 1주차 문제해설
- [1904 - 01타일](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/1904.py "1904 - 01타일")
- [1912 - 연속 합](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/1912.py "1912 - 연속 합")
- [2156 - 포도주 시식](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/2156.py "2156 - 포도주 시식")
- [9184 - 신나는 함수 실행](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/9184.py "9184 - 신나는 함수 실행")
- [10844 - 쉬운 계단 수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/10844.py "10844 - 쉬운 계단 수")
- [11053 - 가장 긴 증가하는 부분 수열](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/11053.py "11053 - 가장 긴 증가하는 부분 수열")
- [14888 - 연산자 끼워넣기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/14888.py "14888 - 연산자 끼워넣기")
- [14889 - 스타트와 링크](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/14889.py "14889 - 스타트와 링크")
---
해설 없는 문제

---
## [1011 - Fly me to the Alpha Centuri](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/1011.py "1011 - Fly me to the Alpha Centuri")
- 시간제한 : 2초 | 메모리제한 : 512MB

실제로 거리에 따른 최소 공간이동 횟수를 나열해보면 [1 2 33 44 555 666 ...] 같은 규칙성을 내포하고 있다는 것을 알 수 있다.

| 거리  | 최소 횟수 |
|:-----:|:--------:|
|1      | 1        |
|2      | 2        |
|3      | 3        |
|4      | 3        |
|5      | 4        |
|6      | 4        |
|7      | 5        |
|8      | 5        |
|9      | 5        |

1,2번이 1개, 3,4번이 2개, 5,6번이 3개.. 이런식으로 반복되므로 `dist`로 서로의 거리 차이를 구하고 이 수가 어느 구간에 속하는지 보아야 한다.
```python
while dist > sig[i]:
    i += 1
    sig.append(sig[i-1] + i*2)
```
위 반복문을 통해 `dist`가 몇개가 반복되는 구간에 속하는지 확인하고 
```python
if dist <= ((sig[i] + sig[i-1]) // 2):
    print(i * 2 - 1)
else:
    print(i * 2)
```
이를 통해 결과를 출력하면 된다

---
## [3053 - 택시 기하학](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/3053.py "3053 - 택시 기하학")
- 시간제한 : 1초 | 메모리제한 : 128MB

거리를 `x`와`y` 각각의 차이를 더한 값으로 둔다고 했을때 원의 정의는 한 점으로부터 거리가 같은 점들의 집합이므로 원점을 중심으로 하며 `x+y = 입력한 수`를 하는 정사각형으로 생각하면 된다. 이는 결국 `(2*입력한수)² / 2`이므로 `입력한 수 * 입력한 수 * 2`와 같다.
```python
print("%.nf" % float)
```
`n`자릿수만큼 `float`를 표현하겠다는 서식문자를 통해 정답을 출력해주면 된다.

---
## [4948 - 베르트랑 공준](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/4948.py "4948 - 베르트랑 공준")
- 시간제한 : 1초 | 메모리제한 : 256MB

에라토스테네스의 채 알고리즘을 사용해 `123456 * 2`보다 큰 `250000`까지의 소수 배열을 구하고
```python
range(num + 1, 2 * num + 1)
```
를 선형탐색하며 소수가 있을때마다 `sum += 1`을 해주면 정답을 알 수 있다. 
---
## [2447 - 별찍기 10](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/2447.py "2447 - 별찍기 10")
- 시간제한 : 1초 | 메모리제한 : 256MB

처음 입력한 수가 3의 몇 제곱수인지 구하고 이를 `ln`이라고 칭하자. 그렇다면 가운대 공백은 `3** (ln-1)`만큼 생길 것이고 이를 공백으로 처리하는 `makeBlank`함수를 생성해서 가운데 공백처리를 해주고, 만약 남은 구역이 있다면 남은 8개의 구역마다 `makeBlank()`재귀함수를 실행시키면 된다. 

---
## [15649 - N과 M(1)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/15649.py "15649 - N과 M(1)")
- 시간제한 : 1초 | 메모리제한 : 512MB

백트래킹 알고리즘으로 풀 수 있다.
```python
for i in range(1,n+1): #1부터 n까지
    if i in s:  #s 안에 같은 수가 있으면 다음 수로 넘어감
        continue
    s.append(i)
    printm() # 숫자 4개의 조합은 1개를 고르고 나머지 중에서 3개를 고르는것과 같으므로, 위에서 1개를 골랐으므로 나머지를 다시 고르는 재귀의 형식으로 구하면 된다.
    s.pop()
```
이를 통해 재귀를 반복하다가 `len(s) == m`의 조건을 만족하면 이는 한개의 조합을 생성했다는 것이므로, 이를 출력하고 `s.pop()`을 통해 다른 수를 넣어보는 방식으로 정답을 출력할 수 있다.

나머지 N과 M(2),(3),(4) 또한 조금의 수정을 거쳐서 풀 수 있으므로 설명은 생략한다.

---
## [9663 - N-Queen](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/9663.py "9663 - N-Queen")
- 시간제한 : 10초 | 메모리제한 : 128MB

N과 M(1)과 같은 백트래킹 알고리즘으로 문제를 풀 수 있다.
우선 퀸은 같은 행, 같은 열을 모두 공격할 수 있으므로 한 행, 한 열에는 한개의 퀸만 존재한다는 것이 자명하다.
```python
def setQueen(row):
    global cnt
    if len(queenpos) == size:
        cnt += 1
        return 
    else:
        for y in range(size):
            if not checkPos(row,y):
                continue
        queenpos.append((row,y))
        setQueen(row+1)
        queenpos.pop()
```
`queenpos`에 저장된 퀸의 위치좌표 갯수가 `size`와 같아졌다면 모든 퀸의 배열이 완료되었다는 의미이므로 `cnt`를 하나 늘린다. 만약 같지 않다면 이는 퀸의 배치가 아직 완료되지 않았다는 의미이므로 `row`내 모든 위치에서 `checkPos`함수를 통해 가능 여부를 확인, 이를 `queenpos`에 저장한후 다음 열로 넘어가면 된다.

`checkPos`함수는 `queenpos`내 저장된 퀸의 좌표들이 새로운 위치를 공격하는지 여부를 판단하는데, 각 퀸마다 새로운 위치에 대해서 4 중 하나라도 만족한다면 공격이 가능하다는 의미이므로 `False`를 리턴해주고, 이를 하나도 만족하지 않으면 공격하지 않는다는 의미이므로 `True`를 리턴해야한다. 
- 같은 열에 있는지
- 같은 행에 있는지
- 본인의 x,y좌표와 합값이 같은지(y = -x + k 와 같은 선상에 있는 점인지 확인)
- 본인의 x,y좌표와 차이값이 같은지(y = x + k 와 같은 선상에 있는 점인지 확인)

---
## [2580 - 스도쿠](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_4/2580.py "2580 - 스도쿠")
- 시간제한 : 1초 | 메모리제한 : 256MB

```python
def setZero(idx):
    global isPrinted
    if isPrinted:
        return  
    if idx == len(zeropos):
        for i in sudoku:
            print(" ".join(list(map(str,i))))
        isPrinted = True
        return
    else:
        for i in range(1,10):
            if not checkPos(zeropos[idx],i):
                continue
            ans.append((zeropos[idx],i))
            sudoku[zeropos[idx][0]][zeropos[idx][1]] = i
            setZero(idx+1)
            pos,num = ans.pop()
            sudoku[pos[0]][pos[1]] = 0
```
N-Queen과 같은 방법으로 풀면 된다. 주의 할 점은 숫자를 넣을 수 있다면 이를 `sudoku` 배열에 넣고, 만약 중간에 백트래킹 하게 된다면 다시 이 위치를 0으로 돌려놔야한다.
`isPrinted` 전역변수를 통해 출력여부를 확인하고 만일 출력되었을시에 함수를 종료하면 시간을 줄일 수 있다.

---