from sys import stdin

input = stdin.readline
N = int(input())

DP = [0] * (N + 1)

if N == 1:
    print(1)
else:
    DP[1:3] = [1, 3]
    for i in range(3, N + 1):
        DP[i] = (DP[i-1] + DP[i-2] * 2) % 10007
    print(DP[-1])