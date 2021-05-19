# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(K, words):
    line = len(words[0])
    answer = 1
    for word in range(1,len(words)): 
        if line + len(words[word]) + 1 > K:
            line = len(words[word])
            answer += 1
        else:
            line += len(words[word]) + 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")