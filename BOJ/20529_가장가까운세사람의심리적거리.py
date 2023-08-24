from sys import stdin
from itertools import combinations as combi

def check(A, B):
    count = 0
    for i in range(4):
        if A[i] != B[i]:
            count += 1

    return count

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
            distance = min(distance, check(A, B) + check(A, C) + check(B, C))
            if distance == 0:
                break
        print(distance)