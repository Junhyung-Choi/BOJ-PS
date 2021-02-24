# 2월 3주차 문제해설
- [2178 - 미로 탐색](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/2178.py "2178 - 미로 탐색")
- [2667 - 단지번호붙이기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/2667.py "2667 - 단지번호붙이기")
- [9205 - 맥주 마시면서 걸어가기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/9205.py "9205 - 맥주 마시면서 걸어가기")
- [11286 - 절댓값 힙](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/11286.py "11286 - 절댓값 힙")
- [1107 - 리모컨](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/1107.py "1107 - 리모컨")
- [9019 - DSLR](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/9019.py "9019 - DSLR")
- [10026 - 적록색약](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/10026.py "100`26 - 적록색약")
- [11403 - 경로찾기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/11403.py "11403 - 경로찾기")
- [15686 - 치킨 배달](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/15686.py "15686 - 치킨 배달")
- [16236 - 아기상어](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/16236.py "16236 - 아기상어")

  
---
해설 없는 문제

[7596 - 토마토](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/7596.py "7596 - 토마토") | 
[11047 - 동전 0](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/11047.py "11047 - 동전 0") | 
[14500 - 테트로미노](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/14500.py "14500 - 테트로미노")  | 
[11286 - 절댓값 힙](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/11286.py "11286 - 절댓값 힙") | 
---
## [2178 - 미로 탐색](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/2178.py "2178 - 미로 탐색")
- 시간제한 : 1초 | 메모리제한 : 192MB

BFS를 통해서 풀면 된다. `time`에 각 칸마다 걸리는 최소 시간을 방문 할때마다 갱신하고, `(N,M)`에 도착했을때의 시간을 출력하면 정답을 구할 수 있다.

---
## [2667 - 단지번호붙이기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/2667.py "2667 - 단지번호붙이기")
- 시간제한 : 1초 | 메모리제한 : 128MB

BFS를 사용해서 문제를 풀 수 있다. `matrix`에 배열을 입력받고, 선형 탐색을 실시하며 `matrix[y][x] == 1 and visited[y][x] == 0`의 조건문이 참일때마다 해당하는 위치에서 BFS를 실시하고 탐색이 끝나면 `cnt[]`에 각 단지에 속하는 집의 개수를 `append()` 시키면 `len(cnt)`로 단지의 수를, 각 단지마다 해당하는 집의 개수를 얻을 수 있다.

---
## [9205 - 맥주 마시면서 걸어가기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/9205.py "9205 - 맥주 마시면서 걸어가기")
- 시간제한 : 1초 | 메모리제한 : 128MB

50m당 1병을 마시고 20병씩 들고 다닐 수 있다면 편의점에 들리지 않고 상근이와 친구들이 걸어갈 수 있는 거리는 1000m이다. 편의점과 펜타포트 락 페스티벌의 좌표를 `stores` 배열에 저장 후 1000m거리 이내에 있는 좌표들로 완전탐색을 반복, 만일 펜타포트 락 페스티벌 좌표에 도착하면 탐색을 종료 및 `happy`를 출력, 만일 탐색이 끝나고 펜타포트에 도착하지 못했다면 `sad`를 출력하면 된다.

---
## [1107 - 리모컨](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/1107.py "1107 - 리모컨") 
- 시간제한 : 2초 | 메모리제한 : 256MB

입력 가능한 숫자 중 입력할 수 있는 숫자만을 지닌 수를 선형 탐색하면서, 최소한의 버튼 값을 매번 갱신해주면 된다.

---
## [9019 - DSLR](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/9019.py "9019 - DSLR")
- 시간제한 : 6초 | 메모리제한 : 256MB

매번 함수를 통해 판별을 할 시에 메모리가 증가하므로 각 조건문을 수식으로 지정, 매번 문자열로 바꿔서 L,R연산을 실시하면 시간이 엄청 늘어남

---
## [10026 - 적록색약](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/10026.py "100`26 - 적록색약")
- 시간제한 : 1초 | 메모리제한 : 128MB

RGB를 나눠서 카운트하는 BFS, R과G를 동일하게 처리하는 RGBFS함수를 구현해서 따로따로 카운트 해주면 된다.

---
## [11403 - 경로찾기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/11403.py "11403 - 경로찾기")
- 시간제한 : 1초 | 메모리제한 : 256MB

그래프에 가중치가 없고 방향 그래프이다. 그러므로 각 노드마다 BFS를 실행하여 도착 가능한 노드를 새로 표시해주면 된다. 시작할때 본인의 위치는 0으로 시작해둬야 한다

---
## [15686 - 치킨 배달](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/15686.py "15686 - 치킨 배달")
- 시간제한 : 1초 | 메모리제한 : 512MB

n개의 치킨 집 중 M개를 고르는 모든 경우의 수를 combination을 통해 구하고, 최솟값을 탐색 한뒤 출력해주면 된다.

---
## [16236 - 아기상어](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_3/16236.py "16236 - 아기상어")
- 시간제한 : 2초 | 메모리제한 : 512MB

상어가 있는 위치에서 계속 BFS 를 실행한다. BFS함수가 각 물고기마다의 도달 여부 및 소요 시간을 timemat으로 넘겨주면 minFind()가 최좌상단에 있는 위치까지 걸리는 시간 및 좌표를 업데이트 하고 내보낸다. 최솟값이 갱신되지 않았다면 먹을 수 있는 물고기가 없다는 의미이므로 함수를 종료하고 엄마상어를 호출(== 걸린 시간 출력)하면 된다.

---