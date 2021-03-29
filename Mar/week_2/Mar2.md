# 3월 2주차 문제해설
- [1010 - 다리놓기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/1010.py "1010 - 다리놓기") | 
- [1037 - 약수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/1037.py "1037 - 약수") | 
- [2004 - 조합 0의 개수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/2004.py "2004 - 조합 0의 개수") | 
- [2565 - 전깃줄](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/2565.py "2565 - 전깃줄") | 
- [2981 - 검문](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/2981.py "2981 - 검문") | 
- [9251 - LCS](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/9251.py "9251 - LCS") | 
- [11051 - 이항계수2](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/11051.py "11051 - 이항계수2") | 
- [12865 - 평범한 배낭](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/12865.py "12865 - 평범한 배낭") | 
- [13305 - 주유소](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/13305.py "13305 - 주유소") | 

---
해설 없는 문제
## [11051 - 이항계수2](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/11051.py "11051 - 이항계수2")
- 1010번과 같은 방식으로 구할 수 있다.

---
## [1010 - 다리놓기](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/1010.py "1010 - 다리놓기")
- 시간제한 : 0.5초 | 메모리제한 : 128MB

다리끼리는 겹쳐질 수 없다고 하며 동쪽의 다리가 항상 많으므로 동쪽의 다리에서 서쪽의 다리개수만큼 사이트를 선정하고 위에서부터 각각 서쪽의 사이트를 한개씩 지정해주면 다리를 만들 수 있다.   결론은 동쪽의 다리에서 서쪽의 다리 갯수만큼 사이트를 고르는 경우의 수를 구하면 되는 것이다. 조합을 사용해서 풀면 구할 수 있다.   파이썬에선 큰 수의 연산이 자유롭지만, 다른 언어의 방식을 빌려보자면 `comb(n,c) = comb(n-1,c-1) + comb(n-1,c)`같은 재귀함수의 형식으로 판단 가능하므로 이를 통해 수를 구하면 된다.

---
## [1037 - 약수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/1037.py "1037 - 약수")
- 시간제한 : 2초 | 메모리제한 : 512MB

진짜 약수의 정의란 N의 약수중 1과 N을 제외한 다른 약수들을 의미한다. 진짜 약수가 모두 주어진다고 했을때 만약 이 수가 제곱수가 아니면 짝수, 제곱수라면 홀수의 갯수가 나오므로 진짜 약수의 갯수의 짝,홀 판별을 통해 가운데 요소를 두번 곱할것인지, 양 끝의 요소를 곱할 것인지 판단 후 결과를 도출하면 된다.

---
## [2004 - 조합 0의 개수](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/2004.py "2004 - 조합 0의 개수")
- 시간제한 : 2초 | 메모리제한 : 128MB

조합 nCm은 `math.factorial(n) // (math.factorial(n-m) * math.factorial(m))`으로 표현 가능하다. 아래 수를 소인수 분해한 것 중 2와 5의 개수, 위에서의 2와 5의 개수를 판단하여 위에서 아래를 빼고 2와 5중 작은 수를 출력하면 된다. 

---
## [2565 - 전깃줄](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/2565.py "2565 - 전깃줄")
- 시간제한 : 1초 | 메모리제한 : 128MB

가장 적은 전깃줄을 제거하여 전깃줄이 교차하지 않게 하려면 교차하지 않는 가장 긴 전깃줄 배열을 구하면 된다. 시작하는 번호를 작은 순서대로 정렬하고, 위에서부터 본인 위에 있는 전깃줄 중 겹치지 않을때 그 전깃줄까지의 안겹치는 수 + 1들중 가장 큰 수를 본인까지의 안겹치는수로 정하고 이를 끝까지 진행하면 최대한 안겹치고 고를 수 있는 전깃줄의 개수가 나온다. 전체 전깃줄의 개수 중 최대 갯수를 뺀 값을 출력하면 최소한으로 제거해야하는 전깃줄 수를 구할 수 있다.

---
## [2981 - 검문](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/2981.py "2981 - 검문")
- 시간제한 : 1초 | 메모리제한 : 128MB

각 수를 특정 수로 나누었을때 나머지가 같다고 하면 `data[i] - (data[i] // m) * m == data[i+1] - (data[i+1] // m) * m` 이란 뜻이고 이를 다시 쓰면 `data[i+1] - data[i] == m * (data[i+1] // m - data[i] //m)`으로 표현할 수 있다. 모든 i에 대해 이가 성립하므로 붙어있는 두 수들의 차이는 m으로 나누어떨어진다는 것을 알 수 있으므로, 두 수들의 차이의 최대공약수를 구한 후 이의 약수를 출력해주면 된다.

---
## [9251 - LCS](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/9251.py "9251 - LCS")
- 시간제한 : 1초 | 메모리제한 : 128MB

두개의 수열이 주어졌을때 모두의 부분수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

|   | 0 | a | c | a | y | k | p |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| c | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| a | 0 | 1 | 1 | 2 | 2 | 2 | 2 |
| p | 0 | 1 | 1 | 2 | 2 | 2 | 3 |
| c | 0 | 1 | 2 | 2 | 2 | 2 | 3 |
| a | 0 | 1 | 2 | 3 | 3 | 3 | 3 |
| k | 0 | 1 | 2 | 3 | 3 | 4 | 4 |

위의 표는 위치하는 곳까지의 LCS수를 나열한 것이다. (1,1) 같은경우 a 와 ca 까지의 LCS 길이이므로 1이 되겠다. 이 수를 구하는 것은 다음과 같은 점화식으로 표현이 가능하다
- 열과 행의 값이 같을 경우 (열-1)(행-1)의 수 + 1
- 열과 행의 값이 다를 경우 max((열-1)(행),(열)(행-1))

왜냐하면 ABC 와 DAC를 비교했을때 ABC와 DAC까지의 LCS는 마지막이 같으므로 AB와 DA의 LCS 값에서 + 1을 해주면 된다. 그러나 ABC와 DA의 LCS를 구한다고 C와 A를 뺀 AB와 D를 비교하게 되면 ABC에 있는 A와 DA의 마지막에 있는 A를 LCS에 포함할 수 없게 되므로, 각자의 마지막을 하나씩만 뺀 ABC와 D까지의 LCS, AB와 DA까지의 LCS를 보면서 더 긴 쪽을 사용해야 한다. 

---
## [12865 - 평범한 배낭](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/12865.py "12865 - 평범한 배낭")
- 시간제한 : 2초 | 메모리제한 : 512MB

이 문제는 knapsack 알고리즘이라고 이름이 따로 있을 정도로 유명한 문제 중 하나이다.    
우선 최대 무게까지만큼의 크기를 가진 배열을 각 물건 갯수만큼 만들어준다.
그 후 dp[아이템][무게] 인 배열을 만들어 주자.   
이 배열은 각 아이템 index 까지의 아이템들과 무게 index까지로 구성된 최대 가치를 저장한다.   
초기값은 다 0으로 만들어두고 첫번째 아이템부터 최대 무게가 본인 무게보다 적거나 같다면 그 전 아이템까지 본인의 무게를 뺀 `(dp[아이템-1][무게-본인무게])`의 가치와 본인을 더한 것이랑 해당 무게까지 본인 전 아이템까지의 최대가치`(dp[아이템-1][무게])`를 비교해서 본인이 들어가는것과 안들어가는 것중 최댓값을 구해 본인까지의 최댓값으로 설정해주면 된다는 이야기이다.

```python
dp[itemidx][weight] = max(curitemval + dp[itemidx-1][weight - curitemweight],dp[itemidx-1][weight])
```

이를 마지막 아이템까지 실행 한 후 마지막 행의 마지막 값을 출력하면 결과를 얻을 수 있다.

---
## [13305 - 주유소](https://github.com/Junhyung-Choi/BOJ-PS/blob/master/Mar/week_2/13305.py "13305 - 주유소")
- 시간제한 : 2초 | 메모리제한 : 512MB

처음부터 그보다 기름 값 적은 도시까지 가는 만큼 기름 사고, 그 다음 도시에서 더 적은 곳까지만 기름 사고 해서 최소값으로 문제 해결하면 된다.

---
