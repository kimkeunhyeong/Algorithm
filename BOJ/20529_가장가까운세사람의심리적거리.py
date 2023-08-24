from sys import stdin
from itertools import combinations as combi

# 미리 거리를 계산하여 중복 계산 방지
# -> 실행시간 288ms(60%) 감소
types = "ISTJ, ISFJ, INFJ, INTJ, ISTP, ISFP, INFP, INTP, ESTP, ESFP, ENFP, ENTP, ESTJ, ESFJ, ENFJ, ENTJ".split(", ")
mapping_str = {value:index for index, value in enumerate(types)}
mapping_num = {index:value for index, value in enumerate(types)}

distance_table = [[0] * 16 for i in range(16)]
for i in range(16):
    for j in range(16):
        if i == j:
            continue
        if not distance_table[i][j]:
            diff = 0
            for k in range(4):
                if mapping_num[i][k] != mapping_num[j][k]:
                    diff += 1
            distance_table[i][j] = distance_table[j][i] = diff

input = stdin.readline

TC = int(input())

for _ in range(TC):
    num_student = int(input())
    students = input().rstrip().split()
    if num_student > 32: # 16개의 성격이 2명씩 있다고 할때, 최대. 이후는 무조건 한 성격이 3명인 경우가 있음
        print(0)
    else:
        distance = 999999
        for A, B, C in combi(students, 3):
            a, b, c = mapping_str[A], mapping_str[B], mapping_str[C]
            distance = min(distance, distance_table[a][b] + distance_table[a][c] + distance_table[b][c])
            if distance == 0:
                break
        print(distance)