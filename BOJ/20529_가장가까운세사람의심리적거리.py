from sys import stdin
from collections import Counter
from math import comb
from itertools import combinations as combi

input = stdin.readline

TC = int(input())

for _ in range(TC):
    input()
    students = Counter(input().rstrip().split())
    distance = []
    for i in students.values():
        if i > 1:
            distance += [0] * comb(i, 2)
    for A, B in combi(students.keys(), 2):
        temp_dist = 0
        for i in range(4):
            temp_dist += (A[i] != B[i])

        distance += [temp_dist] * students[A] * students[B]
        print(distance)
    distance.sort()
    print(sum(distance[:3]))