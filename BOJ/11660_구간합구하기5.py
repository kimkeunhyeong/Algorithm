from sys import stdin
from copy import deepcopy
input = stdin.readline

size, TC = map(int, input().split())
data = [list(map(int, input().split())) for i in range(size)]
sum_data = deepcopy(data)

for i in range(1, size):
    sum_data[0][i] += sum_data[0][i-1]
    sum_data[i][0] += sum_data[i-1][0]
    
for i in range(1, size):
    for j in range(1, size):
        sum_data[i][j] += sum_data[i-1][j] + sum_data[i][j-1] - sum_data[i-1][j-1]

for i in range(TC):
    start_row, start_col, end_row, end_col = [i - 1 for i in map(int, input().split())]
    result = sum_data[end_row][end_col]
    double = False
    if start_row != 0:
        result -= sum_data[start_row - 1][end_col]
        double = True
    if start_col != 0:
        result -= sum_data[end_row][start_col - 1]
        if double:
            result += sum_data[start_row - 1][start_col - 1]
    print(result)