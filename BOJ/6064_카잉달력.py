from sys import stdin
from math import lcm

def get_result(M, N, x, y):
    year = x
    MAX_year = lcm(M, N)
    while year <= MAX_year:
        x_prime, y_prime = year % M, year % N
        if not x_prime:
            x_prime = M
        if not y_prime:
            y_prime = N

        if x == x_prime and y == y_prime:
            return year
        year += M

    return -1
input = stdin.readline

TC = int(input())
for i in range(TC):
    M, N, x, y = map(int, input().split())
    if M > N: # 왼쪽이 무조건 작도록 swap해줌
        M, N, x, y = N, M, y, x

    print(get_result(M, N, x, y))