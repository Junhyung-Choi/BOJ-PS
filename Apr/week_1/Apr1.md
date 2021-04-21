# 4월 1주차 문제해설
[13549 - 숨바꼭질 3](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/13549.py "13549 - 숨바꼭질 3") | 
[14502 - 연구소](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/14502.py "14502 - 연구소") | 
[2740 - 행렬 곱셈](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/2740.py "2740 - 행렬 곱셈") | 
[2033 - 반올림](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/2033.py "2033 - 반올림") | 
[17070 - 파이프 옮기기 1](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/17070.py "17070 - 파이프 옮기기 1") |  
[17144 - 미세먼지 안녕!](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/17144.py "17144 - 미세먼지 안녕!") | 

---
해설 없는 문제

[2740 - 행렬 곱셈](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/2740.py "2740 - 행렬 곱셈")   
그냥 곱하면 된다.

[2033 - 반올림](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/2033.py "2033 - 반올림")   
round가 불안정하므로 그냥 반올림 구현해주면 된다.


---
## [13549 - 숨바꼭질 3](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/13549.py "13549 - 숨바꼭질 3")
- 시간제한 : 2초 | 메모리제한 : 512MB

숨바꼭질2와는 다르게 *2는 시간이 걸리지 않으므로 time을 갱신하지 않고, 또한 +1,-1보다 이동하는 시간이 적으므로 큐의 앞에 둬야한다.

---
## [14502 - 연구소](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/14502.py "14502 - 연구소")
- 시간제한 : 2초 | 메모리제한 : 512MB

가능한 모든 위치를 백트래킹을 통해서 모든 벽을 세우고 벽이 3개 될때마다 BFS 알고리즘을 통해 max_result를 갱신해서 안전영역의 최댓값을 알아낸다.

---
## [17070 - 파이프 옮기기 1](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/17070.py "17070 - 파이프 옮기기 1")
- 시간제한 : 1초 | 메모리제한 : 512MB

다음 방향이 가로일때는 이전 방향이 가로, 대각선인 경우이다.
다음 방향이 세로일때는 이전 방향이 세로, 대각선인 경우이다.
다음 방향이 대각선일때는 이정 방향이 가로, 세로, 대각선 모든 경우에서 가능하다.
파이프의 오른쪽, 혹은 아래쪽 칸을 기준으로 DFS를 통해 끝까지 가는 모든 경우를 카운트하고 이를 출력해주면 된다.

---
## [17144 - 미세먼지 안녕!](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Apr/week_1/17144.py "17144 - 미세먼지 안녕!")
- 시간제한 : 1초 | 메모리제한 : 512MB

미세먼지가 확장하는 `expand()`와 공기청정기가 작동하는 `cleaner()`를 구현 한 후 이를 원하는 횟수만큼 돌려주면 된다.

`expand()`를 구현할때 기존 matrix에 바로 변경점을 반영 할시에는 여러개의 먼지가 동시에 작용하는 칸의 계산이 복잡해지므로, 원래 값을 보존하되 변경되는 값들을 copy 매트릭스에 보관 후 함수가 끝날때 일괄 반영해주는 방법으로 진행했다.

`cleaner()`를 구현할 때 위를 도는 구간이랑 아래를 도는 구간을 나눠서 구현했다.

---
