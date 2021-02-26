# 2월 2주차 문제해설
- 1697 - 숨바꼭질
- 7576 - 토마토
- 7662 - 이중 우선순위 큐
- 17626 - Four Squares 
- 1780 - 종이의 개수
- 1389 - 케빈 베이컨의 6단계 법칙
- 5525 - IOIOI
- 9375 - 패션왕 신해빈
- 17219 - 비밀번호 찾기

---
해설 없는 문제


[1927 - 최소 힙](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/1927.py "1927 - 최소 힙") | 
[1541 - 잃어버린 괄호](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/1541.py "1541 - 잃어버린 괄호") | 
[1676 - 팩토리얼 0의 개수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/1676.py "1676 - 팩토리얼 0의 개수") |

---
## 1697번 - 숨바꼭질
- 시간제한 : 2초 | 메모리제한 : 128MB

BFS를 이용하여 수빈이가 갈 수 있는 좌표들을 완전 탐색 한 후 발견하였을 시의 시간을 출력하면 된다. 수빈이가 다음 점으로 가면 그 이전의 점까지 걸린 시간보다 1초를 더해서 각 위치마다 걸리는 시간을 측정하고, 수빈이와 동생이 만났을 시에 반복문을 종료시켜 현재 좌표까지 걸린 시간이 최단 시간이다.

[1697 - 숨바꼭질](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/1697.py "1697 - 숨바꼭질")

---
## 7576번 - 토마토
- 시간제한 : 1초 | 메모리제한 : 256MB

익은 토마토가 있는 위치를 큐에 넣은 후 이들을 기준으로 bfs를 돌리면 된다. 그 후 주위에 있는 익지 않은 토마토들을 선택한 뒤 1로 만들고, 큐에 넣은 후 영향을 준 토마토가 익은 날짜에 하루를 더해 익은 날짜를 기록한다. 완전 탐색이 끝난 후 토마토가 저장된 `matrix`에 익지 않은 토마토가 있을 시 `-1`을 출력, 그렇지 않다면 가장 큰 수를 출력한다.

[7576 - 토마토](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/7576.py "7576 - 토마토") 

---
## 7662번 - 이중 우선순위 큐
- 시간제한 : 6초 | 메모리제한 : 128MB

- 우선순위 큐 : 일반적인 큐(Queue)는 First-In-First-Out(FIFO)구조, 먼저 들어온 노드가 먼저 나가는 구조이다. 우선순위 큐란 이 자료들이 우선순위를 부여받아, 들어온 순서에 상관 없이 우선순위가 높은 자료가 먼저 큐에서 나오는 자료구조를 의미한다. 우선순위 큐는 힙(Heap)을 이용해 구현하는데, 최대 힙, 최소 힙 등의 자료구조를 이용하면 최대,최솟값을 위에 둘 수 있고, 이를 통해 우선순위가 최대인 자료를 빠르고 쉽게 접근 할 수 있기 때문이다.
- 이중 우선순위 큐는 우선순위가 제일 높거나 낮은 데이터를 원하는 대로 출력할 수 있는 큐이다. 각각 최대, 최소 힙을 만들어서 데이터를 인덱스와 같이 추가하고, 데이터를 빼는 연산을 진행할때, 각각 다른 힙에서 빠졌던 노드는 `visited` 리스트에 기록되어 무시하고 그 다음 노드를 출력하는 방식으로 진행하면 답을 구할 수 있다. 최대,최소 힙에서 자료를 더하거나, 빼는 방법은 2월 1주차 최대 힙에서 설명했으므로 넘어간다.

[7662 - 이중 우선순위 큐](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/7662.py "7662 - 이중 우선순위 큐") 

---
## 17626번 - Four Squares
- 시간제한 : 0.5초 | 메모리제한 : 512MB

문제에 의하면 모든 자연수는 넷 혹은 그 이하의 제곱수로 표현된다. 그러므로 `0`과 `1`을 제외한 모든 수의 최소 제곱수 개수를 `5`로 초기화 한다. `n`을 입력받은 후 `for i in range(2,n+1)`로 반복문을 실행하며 `i`보다 작은 수`j`(`j`는 `sqrt(i)`보다 크면 안된다.)로 반복문을 실행하며 `tmp = i - (j**2)`를 구하고 `arr[tmp]`값이 제일 작은 것을 구하면 n을 만드는 `j`와 가장 적은 제곱수로 구성된 `tmp`를 구할 수 있으므로 n을 최소의 제곱수로 구성하는 값을 알 수 있다.

[17626 - Four Squares](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/17626.py "17626 - Four Squares") 

---
## 1780번 - 종이의 개수
- 시간제한 : 2초 | 메모리제한 : 256MB

`[+1,0,-1]` 각각의 원소에 해당하는 종이의 개수를 셀 변수를 `[p,z,m]`로 두고 본인의 모든 원소를 탐색하는 재귀함수 `nineRecur()`을 만든다. 만약 전에 탐색한 원소와 다른 값이 나오면 이는 다른 종이가 중간에 끼어있다는 의미이므로 9개의 구역으로 나눠서 다시 `nineRecur()`을 진행시키면 된다. 다른 값이 나오지 않았다면 모든 숫자들을 더한 `tmp`의 값이 `size`의 제곱인지, 0인지, 음수제곱인지 확인하면 각각 `[1,0,-1]`로 이루어져있는지 확인 할 수 있다. 그 후 `[p,z,m]` 중 맞는 변수에 1을 더해주면 된다.

[1780 - 종이의 개수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/1780.py "1780 - 종이의 개수")

---
## 1389번 - 케빈 베이컨의 6단계 법칙
- 시간제한 : 2초 | 메모리제한 : 128MB

각 유저만큼의 숫자에 1을 더한 만큼을 변의 길이로 하는 정사각행렬 `matrix`를 만든다.(1을 더하는 이유는 입력받는 노드의 번호를 행렬의 index로 사용하기 위해서이다.) 그 후 링크를 입력받으면 양방향 링크이므로 `matrix[usera][userb]` 와 `matrix[userb][usera]`를 이용해 연결됨을 `1`로 표현한다. 그 후 모든 사람에 대해 bfs를 실행한 후 한 사람이 각 유저마다 걸리는 시간을 `cnt`에 기록하고, 이를 전부 더한 값을 `bacon`에 저장함으로써 모든 사람의 케빈베이컨 수를 구할 수 있고, 이중 가장 작은 값을 `min()`을 통해 알아낸 뒤 `index()`함수를 통해 가장 작은 케빈 베이컨수를 가진 사람들 중 가장 작은 번호를 부여받은 사람을 구할 수 있다.

[1389 - 케빈 베이컨의 6단계 법칙](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/1389.py "1389 - 케빈 베이컨의 6단계 법칙") 

---
## 5525번 - IOIOI
- 시간제한 : 1초 | 메모리제한 : 256MB

P1 = "IOI" | P2 = "IOIOI" | P3 = "IOIOIOI" 등을 볼때 각각 `IOI`가 가운데 `I`를 겹치게 n번 반복되는 것을 볼 수 있다. 입력받은 문자열을 처음부터 `i`로 순회하며 `s[i] = "I"`,`s[i+1] = "O"`,`s[i+2]="I"`를 만족하면 1개의 `ioi` 카운트가 올라가고 2개의 index를 올린다. 이 `ioi`카운트가 `n`과 같을 때 `ans` 카운트를 하나 올린다. 그 후 `ioi`카운트를 1개만 줄여줘야 하는데, 그 이유는 n = 2이고 `IOIOIOI`같은 문자열이 있을때 앞의 `IOIOI`를 센 후 뒤의 `IOI`를 세면서 `ioi`카운트가 `n`보다 작아 `ans`에 카운트 안되는 일을 방지 하기 위해서이다. 만약 `s[i] = "I"`,`s[i+1] = "O"`,`s[i+2]="I"`를 만족하지 않는다면 `ioi` 카운트를 `0`로 초기화 하고 그 다음 `i`로 넘어가서 반복한다. 이를 `slen - 3`까지 진행해서 모든 문자열을 확인 할 수 있도록 한다.

[5525 - IOIOI](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/5525.py "5525 - IOIOI") 

---
## 9375번 - 패션왕 신해빈
- 시간제한 : 1초 | 메모리제한 : 128MB

그림에서 보듯 종류별 `(종류1 + 1)(종류2 + 1)•••(종류n + 1)-1`로 답을 구할 수 있다. 딕셔너리에 각 종류별로 옷을 집어넣고 모든 종류별 옷의 숫자를 `len(d[k])`로 구한 후 1을 더한 숫자를 곱한 뒤 1을 빼면 답을 구할 수 있다.

[9375 - 패션왕 신해빈](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/9375.py "9375 - 패션왕 신해빈") 

---
## 17219번 - 비밀번호 찾기
- 시간제한 : 5초 | 메모리제한 : 256MB

파이썬 딕셔너리를 사용해 사이트 주소와 비밀번호를 key와 item으로 저장하고 이를 입력에 맞게 출력해주면 된다.

[17219 - 비밀번호 찾기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Feb/week_2/17219.py "17219 - 비밀번호 찾기") 