# 3월 4주차 문제해설
- [1629 - 곱셈](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/1629.py "1629 - 곱셈") | 
- [1991 - 트리 순회](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/1991.py "1991 - 트리 순회") | 
- [2163 - 초콜릿 자르기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/2163.py "2163 - 초콜릿 자르기") | 
- [9465 - 스티커](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/9465.py "9465 - 스티커") | 
- [11725 - 트리의 부모 찾기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/11725.py "11725 - 트리의 부모 찾기") | 
- [15663 - N과 M(9)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/15663.py "15663 - N과 M(9)") | 
- [15666 - N과 M(12)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/15666.py "15666 - N과 M(12)") | 

---
해설 없는 문제

---
## [1629 - 곱셈](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/1629.py "1629 - 곱셈")
- 시간제한 : 0.5초 | 메모리제한 : 128MB

A를 B번 곱한 수를 C로 나누어야 한다. 제한사항은 A와 B,C의 최대 크기가 너무 크다(2147483647) A를 B번 곱한다고 했을때 최악의 상황은 수가 너무 커서 처리 할 수 없을 것이다. 그러므로 나머지의 분배법칙을 사용해야 하는데 
```python
(a*b)%m = ((a%m)*(b%m)) % m
```
을 이용하면 그나마 쉽게 풀 수 있다. B를 반으로 나눠서 만약 B가 홀수라면 B-1번만 곱한 것과 A를 곱한 값을 리턴, 만약 짝수라면 절반의 값으로 재귀 하는 방식으로 풀면 0.5초와 A,B,C에서의 큰 수들을 처리하기 쉽다.

```python
def getCloser(moda, pownum):
    if pownum == 0:
        return 1
    elif pownum == 1:
        return moda
    if (pownum % 2) > 0:
        return getCloser(moda, pownum - 1) * moda
    half = (getCloser(moda, pownum // 2) % c)
    return (half * half) % c
```

---
## [1991 - 트리 순회](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/1991.py "1991 - 트리 순회")
- 시간제한 : 2초 | 메모리제한 : 128MB

처음 문제를 보고 트리랑 노드를 만들어서 구현을 해야겠다고 마음 먹었었다. 그러나 입력이 순서대로 주어진다는 조건이 문제에 없었기에 루트가 되었다가 아닌 노드들이 너무 많이 발생했다. 그래서 그냥 노드만 가지고 문제를 해결했다.

내가 푼 방법은 input으로 받은 정보 중 만들어지지 않은 노드가 있다면 새로이 이를 생성하고, 그렇지 않다면 기존의 것을 불러온다. 그 후 정보를 갱신하고 만약 기존에 있던 노드라면 기존 정보를 갱신, 그렇지 않다면 treenodes에 새로 append 해서 검색이 가능하게 만든다.

preorder,inorder,postorder는 재귀 순서만 바꾸면 쉽게 풀 수 있다. 혹시 몰라 내용을 정리해 보자면   
> preorder : 루트 -> 좌측 -> 우측
> inorder : 좌측 -> 루트 -> 우측
> postorder : 좌측 -> 우측 -> 루트

순서이다.

그러나 문제 풀이들을 보면서 리스트에 넣고 이를 검색하는 방식이 아니라 딕셔너리에 노드를 넣고 이를 찾는 방식으로 시작하면 훨씬 편한걸 알았다. 

```python
class Node:
    def __init__(self,item,left,right):
        self.item = item
        self.left = left
        self.right = right

tree = {}
tree[node] = Node(item,left,right)
```

위 같은 자료구조를 사용하면 Node 안에 들어있는 property값이 곧 tree의 index가 되므로 기존 노드가 있는지 없는지 확인도 안해도 되고, index에러도 발생하지 않는다.

---
## [2163 - 초콜릿 자르기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/2163.py "2163 - 초콜릿 자르기")
- 시간제한 : 2초 | 메모리제한 : 128MB

N x M 사이즈를 1개씩 자를 수 있도록 하는 최소 횟수는
N개를 총 N-1번만큼 뽀개면 N줄을 얻을 수 있다. 이 N줄을 M-1번만큼 뽀개면 총 N x M개의 초콜릿이 나온다. 이를 수식으로 표현하면 N - 1 + N * (M - 1) 이니까 풀면 N - 1 + NM - N 이 된다. 정리하면 NM - 1 이다 입력받고 곱해서 1을 뺀 다음 출력하면 된다.

---
## [9465 - 스티커](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/9465.py "9465 - 스티커")
- 시간제한 : 1초 | 메모리제한 : 128MB

스티커의 품질이 좋지 않아서 한개의 스티커를 떼면 상하좌우가 다 뜯어진다고 한다.
DP를 활용해서 풀었다.
dp[] 라는 배열은 현재 아이템을 뜯는다고 가정하고, 가장 왼쪽부터 현재까지의 최대 점수를 저장한다. 본인을 무조건 뜯어야 하므로 본인과 상하좌우는 뗄 수 없기에 본인과 대각선에 있는 DP 혹은 대각선의 좌측 스티커를 떼는 DP를 고려해야한다. 대각선 좌측을 고려하는 이유는 대각선에 있는 자료가 너무 적어서 이를 안떼고 넘어갈 수 있는 경우를 고려해야한다.
이를 점화식으로 표현하면
```python
data[0][index] = max(data[1][index-1],data[1][index-2]) + data[0][index]
data[1][index] = max(data[0][index-1],data[0][index-2]) + data[1][index]
```

와인 마시기 문제랑 비슷하게 풀 수 있다.

---
## [11725 - 트리의 부모 찾기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/11725.py "11725 - 트리의 부모 찾기")
- 시간제한 : 1초 | 메모리제한 : 256MB

노드들의 크기로 matrix를 하나 만들고, 각 노드의 index마다 부모를 저장할 parents배열을 하나 만든다. 이후 matrix를 bfs 하며 완전탐색을 도는 동안 parents에 부모 정보를 저장 한 뒤 완전탐색이 종료되면 parents배열을 출력해주면 된다.

---
## [15663 - N과 M(9)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/15663.py "15663 - N과 M(9)")
- 시간제한 : 1초 | 메모리제한 : 512MB

이건 꽤 어려웠다. 기존의 N과 M은 중복되는 값이 들어오지 않았는데 이건 중복되는 값이 들어왔고, 한개의 값을 여러번 사용해서도 안되었다. 그러므로 이를 방지하기 위해선
- 한개의 배열에서 사용된 것을 체크하는 check 배열(중복된 값이 들어갈 수 있으므로 배열에 현재 값이 있는지 없는지로 판단 불가능)
- 바로 전에 쓰였던 숫자가 다시 쓰이는걸 확인하는 last 변수(전에 중복된 값을 사용했던 배열과 중복된 결과를 도출하는걸 막기 위함) //깊이가 다를 때마다 이를 초기화 해줘야 함 <- 다른 깊이에서 사용되는 것은 상관 없음

처음엔 이해가 가지 않았는데 여러번 보다보니까 이해가 되는거 같기도 하다.

---
## [15666 - N과 M(12)](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_4/15666.py "15666 - N과 M(12)")
- 시간제한 : 2초 | 메모리제한 : 512MB

얼핏 보면 15663번이랑 같아 보일 수 있지만, 한개의 숫자를 여러번 써도 된다고 하니까 결국 중복된 값을 하나로 다 뭉쳐버리면 되는 문제이다. 파이썬의 set을 활용해서 중복된 값들을 거르고, 이를 정렬 한 후 백트래킹을 이용해서 풀었다.

---
