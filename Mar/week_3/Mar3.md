# 3월 3주차 문제해설
- [1021 - 회전하는 큐](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/1021.py "1021 - 회전하는 큐") | 
- [2407 - 조합](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/2407.py "2407 - 조합") | 
- [15654 - N과 M(5)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/15654.py "15654 - N과 M(5)") | 
- [15657 - N과 M(8)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/15657.py "15657 - N과 M(8)") | 
- [18258 - 큐2](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/18258.py "18258 - 큐2") | 
- [scofe_1_1 - 회전하는 큐](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/1.py "1 - 대여시간을 추천해드립니다.") | 
- [scofe_1_2 - 배송 전략 실험](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/2.py "2 - 배송 전략 실험") | 
- [scofe_1_3 - 상품 배치 추천](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/3.py "3 - 상품 배치 추천") | 
- [scofe_1_4 - 안 본 콘텐츠 없게 해주세요](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/4.py "4 - 안 본 콘텐츠 없게 해주세요") | 
- [scofe_1_5 - 시선 이동](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/5.py "5 - 시선 이동") | 
- [scofe_1_6 - 팝업 스토리](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/6.py "6 - 팝업 스토리") | 

---
해설 없는 문제   
[2407 - 조합](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/2407.py "2407 - 조합") - 3월 2주차 참고

---
## [1021 - 회전하는 큐](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/1021.py "1021 - 회전하는 큐")
- 시간제한 : 2초 | 메모리제한 : 128MB

deque()를 만들고 더 짧은 쪽으로 이동하는 횟수를 구한 뒤 그만큼 옮기고 빼고 하는 식으로 진행하면 된다.

---
## [15654 - N과 M(5)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/15654.py "15654 - N과 M(5)")
- 시간제한 : 2초 | 메모리제한 : 128MB

N개 중 M개를 고르면 되는 문제이다. 백트래킹을 사용하면 쉽게 풀 수 있는데, 다음 요소를 고를때 사용한 것이 기존 배열에 들어있다면 이를 제외하고 다음 반복문을 실행하는 방식으로 풀면 금방 푼다.

---
## [15657 - N과 M(8)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/15657.py "15657 - N과 M(8)")
- 시간제한 : 1초 | 메모리제한 : 128MB

N개 중 M개를 고르면 되는데 기존의 것도 써도 된다. 다음 요소를 고를때 처음부터 고르고 본인보다 크거나 같은 요소들만 넣어서 진행하면 금방 푼다.

---
## [18258 - 큐2](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/18258.py "18258 - 큐2")
- 시간제한 : 1초 | 메모리제한 : 128MB

그냥 큐 구현하면 푼다. deque()모듈 사용하면 됨.

---
## [scofe_1st 1 - 대여시간을 추천해드립니다](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/1.py "1 - 대여시간을 추천해드립니다.")

시작하는 시간, 끝나는 시간을 전부 분 단위로 바꾸고 제일 늦게 시작하는 시간과 제일 일찍 끝나는 시간을 구한다. 만약 제일 일찍 끝나는 시간이 제일 늦게 시작하는 시간보다 이르다면 이는 결국 전원이 공유하는 시간대가 없다는 의미이므로 `-1`을 출력하고 그게 아니라면 형식에 맞춰서 출력해주면 된다.

---
## [scofe_1st 2 - 배송 전략 실험](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/2.py "2 - 배송 전략 실험")

실제로 세보면 피보나치 수열을 따른다고 볼 수 있다. DP 사용해서 풀자

---
## [scofe_1st 3 - 상품 배치 추천](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/3.py "3 - 상품 배치 추천")

`matrix`에 입력을 받고 모든 검정색칸에서 각 사이즈를 대본다. 만약 한 위치에서 가능하다면 그 사이즈의 가능 갯수를 +1 해준다. 이를 사이즈별로 반복 후 결과값을 출력해주면 된다.

---
## [scofe_1st 4 - 안 본 콘텐츠 없게 해주세요](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/4.py "4 - 안 본 콘텐츠 없게 해주세요")

genre 딕셔너리를 만들어서 각 장르("A","B","C","D","E")를 평점과 연결시킨다. 데이터를 입력받고 Y(안본것들) 먼저 추려서 장르 평점이 큰 순서대로 정렬 후 result에 append 해주고 그 후 O인 것들 추려서 반복해주면 풀 수 있다.

---
## [scofe_1st 5 - 시선 이동](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/5.py "5 - 시선 이동")

행렬로 입력을 받은 후 "c"인 지점에서부터 시작한다. 한 점을 기준으로
- (1,0) //아래로 이동
- (0,1) //우측으로 이동
- (0,-1) //좌측으로 이동
이 세가지 방향 중 한곳으로만 움직일 수 있는데, 이전에 움직였던 경로로 가는것은 왔던 길을 되돌아 가는 것이므로 최소길이라는 가정에 모순, 제외해도 되는 경우의 수이다. BFS를 통해 완전탐색을 진행하면 되는데, 탐색을 진행하는 동안 지나는 점까지 좌우 이동을 한 갯수를 `time`배열을 통해 저장해주면서 내려가면 한 시작점에서의 최소 좌우 이동횟수를 알아낼 수 있다.

이 작업을 모든 시작점에서 진행하고 각 시작점끼리의 최소 시작 횟수를 갱신하다 보면 전체적인 최소 시선 이동 횟수를 구할 수 있다. 중간에 막힐 수 있는 경우를 조심해야 하는데, 만약 마지막 층에서의 visited배열 값이 1인 경우가 하나라도 나온다면 이는 마지막까지 닿을 수 있는 경로가 1개라도 있다는 것이고, 이는 곧 막히지 않았음을 증명한다. 이를 통해 결과값을 출력할지, -1을 출력할지 확인 할 수 있다.


---
## [scofe_1st 6 - 팝업 스토리](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_3/scofe2021_1st/6.py "6 - 팝업 스토리")

우로 이동할건지 아래로 이동할 건지 둘중에 하나밖에 없으므로 DP활용해서 풀면 된다. 
```python
for xidx in range(1,xsize+1):
    for yidx in range(1,ysize+1):
        dp[xidx][yidx] = max(dp[xidx-1][yidx],dp[xidx][yidx-1]) + matrix[xidx-1][yidx-1]
```

---