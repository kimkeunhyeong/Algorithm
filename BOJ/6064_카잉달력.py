from sys import stdin
from math import lcm

def get_result(M, N, x, y):
    year = x
    MAX_year = lcm(M, N)
    if y == N:
        # y를 0으로 만들면 반복문 안에서 추가로 검사할 필요가 없음.
        # y_prime이 0일 때의 코드 삭제 후 실행시간 64ms(7%) 추가 감소.
        y = 0
    while year <= MAX_year:
        # 시작을 x부터 시작하고, M만큼 증가하며 검사하니 x를 검사할 필요가 없음.
        # -> x_prime, x 검사 부분 삭제 후 실행시간 528ms(38%) 감소.
        y_prime = year % N

        if y == y_prime:
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