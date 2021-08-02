#BOJ 2096 - 내려가기
import sys
input = sys.stdin.readline

lines = int(input())
max_line = min_line = list(map(int,input().split()))

for index in range(lines-1):
    line = list(map(int,input().split()))
    max_line = [line[0] + max(max_line[0],max_line[1]), line[1] + max(max_line), line[2] + max(max_line[1],max_line[2])]
    min_line = [line[0] + min(min_line[0],min_line[1]), line[1] + min(min_line), line[2] + min(min_line[1],min_line[2])]

print(max(max_line),min(min_line))


# for i in range(1,lines):
#     for j in range(3):
#         if j == 0:
#             matrix[i][0] = matrix[i][0] + max(matrix[i-1][0],matrix[i-1][1])
#         elif j == 1:
#             matrix[i][1] = matrix[i][1] + max(matrix[i-1])
#         elif j == 2:
#             matrix[i][2] = matrix[i][2] + max(matrix[i-1][1],matrix[i-1][2])
# max_score = max(matrix[lines-1])

# for i in range(1,lines):
#     for j in range(3):
#         if j == 0:
#             min_matrix[i][0] = min_matrix[i][0] + min(min_matrix[i-1][0],min_matrix[i-1][1])
#         elif j == 1:
#             min_matrix[i][1] = min_matrix[i][1] + min(min_matrix[i-1])
#         elif j == 2:
#             min_matrix[i][2] = min_matrix[i][2] + min(min_matrix[i-1][1],min_matrix[i-1][2])

# min_score = min(min_matrix[lines-1])

# print(max_score,min_score)
