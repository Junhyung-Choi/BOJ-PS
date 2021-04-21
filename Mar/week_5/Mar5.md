# 3월 5주차 문제해설
[11660 - 구간 합 구하기 5](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/11660.py "11660 - 구간 합 구하기 5") | 
[1753 - 최단경로](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/1753.py "1753 - 최단경로") | 
[16953 - A -> B](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/16953.py "16953 - A -> B") | 
[1916 - 최소비용 구하기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/1916.py "1916 - 최소비용 구하기") | 
[12851 - 숨바꼭질 2](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/12851.py "12851 - 숨바꼭질 2") | 

---
해설 없는 문제

---
## [11660 - 구간 합 구하기 5](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/11660.py "11660 - 구간 합 구하기 5") 
- 시간제한 : 1초 | 메모리제한 : 256MB

위 문제는 N*N 크기의 표에 채워진 숫자들을 빠르게 계산하는게 중점이다. 각 칸마다의 숫자를 계산해 낸 뒤 입력받은 구간의 값을 계산해내면 쉽다.

예를 들어 (2,2)(4,4)까지의 합은 (1,1)(4,4)에서 (1,1)(4,2),(1,1)(2,4) 를 빼고 (1,1)(2,2)를 다시 더한 값과 같으므로 1,1을 기준으로 한 (4,4),(4,2),(2,4),(2,2) 까지의 합을 기존의 계산한 것들을 사용해서 구하면 된다.

---
## [1753 - 최단경로](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/1753.py "1753 - 최단경로")
- 시간제한 : 2초 | 메모리제한 : 256MB

기존에 풀어왔던 무방향 그래프가 아니라, 방향 그래프를 활용해야 한다. 또한 각 간선마다 가중치가 있기 때문에 이를 고려해야 한다.
이 문제는 다익스트라 알고리즘을 사용해서 풀어보았다.
다익스트라 알고리즘이란 한 점에서부터 모든 점까지의 최소 거리를 구할 수 있는 알고리즘이다.
한 점에서 가장 짧은 거리에 있는 점들의 집합을 S로 두고, 다른 점들과의 거리를 S를 통한 거리와 비교, 이를 갱신 후 가장 짧은 거리를 다시 S에 넣고 그 후 진행하는 방식으로 최소 거리들을 찾아내는 것이다.
가중치를 각 노드마다의 거리로 두고, 가장 짧은 것을 빠르게 출력 가능한 최소 힙을 사용했다.

```python
def dijkstra():
    global startnode
    # 시작점 세팅 
    weight[startnode] = 0
    heapq.heappush(heap,(0,startnode))
    # 힙(짧은 거리에 있는 점들의 집합 S를 MinHeap으로 둔다.)
    while heap:
        curweight,curnode = heapq.heappop(heap)
        # 현재까지 갱신된 거리보다(weight) 힙의 최솟값까지의 거리가 더 길면 (curweight) 무시하고 넘어간다.
        if weight[curnode] < curweight:
            continue
        # 현재까지 갱신된 거리보다 힙의 최솟값까지의 거리가 더 짧다면(curweight)
        # 최솟값과 연결된 모든 노드 중
        for goingweight, nextnode in matrix[curnode]:
            # nextweight = 힙 최솟값까지의 거리 + 최솟값에서 다음 노드까지의 거리
            nextweight = curweight + goingweight
            # 만약 nextweight 가 startnode에서 nextnode 까지의 거리보다 짧다면 이는 최솟값이 갱신된 것이므로 전체 노드의 최소거리 배열(weight)를 갱신 및 힙에 넣어준다.
            if nextweight < weight[nextnode]:
                weight[nextnode] = nextweight
                heapq.heappush(heap,(nextweight,nextnode))
```

---
## [16953 - A -> B](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/16953.py "16953 - A -> B")
- 시간제한 : 2초 | 메모리제한 : 512MB

A에서 B로 이동 가능한 방법은 2를 곱하는 것, 1을 수의 가장 오른쪽에 추가하는것 2가지 이다.
BFS를 활용해서 풀면 된다.
이동 가능한 숫자들이 항상 양의 방향으로만 커지므로, B보다 큰 숫자들로 이동했을 시 B로 줄어들 수 없으므로, 이를 큐에 넣지 않은 방식으로 진행한다.
만약 큐가 빌 때까지 B와 같은 수가 나오지 않는다면 이는 B까지 이동할 수 없다는 것을 의미하므로, 기본 출력값을 -1로 두고 B를 만났을 시에 출력값을 갱신해서 출력하면
문제를 풀 수 있다.

---
## [1916 - 최소비용 구하기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/1916.py "1916 - 최소비용 구하기")
- 시간제한 : 0.5초 | 메모리제한 : 128MB

1753번 최단경로와 동일한 풀이이므로 생략하겠다. 

---
## [12851 - 숨바꼭질 2](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_5/12851.py "12851 - 숨바꼭질 2")
- 시간제한 : 2초 | 메모리제한 : 512MB

누나랑 동생 숨바꼭질 문제이다. 1번과 다르게 같은 시간을 통해 몇개의 경로가 있는지를 확인해야한다. 
```python
while queue:
    curpos = queue.popleft()
    if curpos == bpos:
        cnt += 1
    for nextpos in [curpos - 1,curpos + 1,curpos * 2]:
        # 기존 걸리는 시간보다 적거나 같게(동생의 위치에서 같은 시간일때도 체크해줘야 하므로)걸린다면 큐에 추가해준다.
        if nextpos > -1 and nextpos < 100001 and (time[nextpos] == -1 or time[nextpos] >= time[curpos] + 1):
            queue.append(nextpos)
            time[nextpos] = time[curpos] + 1
```

---
