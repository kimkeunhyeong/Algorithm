from sys import stdin

input = stdin.readline
DP = [0] * 101
DP[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    DP[i] = DP[i-1] + DP[i-5]

TC = int(input())
for i in range(TC):
    print(DP[int(input())])