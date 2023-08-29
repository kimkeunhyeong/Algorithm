from sys import stdin
from collections import deque

input = stdin.readline
TC = int(input())

for _ in range(TC):
    current, target = map(int, input().rstrip().split())
    
    DP = [False] * 10000

    Queue = deque([(current, "")])
    DP[current] = True # "" 인 경우 if문에서 False 취급되므로

    while Queue:
        number, string = Queue.popleft()
        if number == target:
            break

        num_D = (number * 2) % 10000
        num_S = number - 1 if number > 0 else 9999
        num_L = (number % 1000) * 10 + number // 1000
        num_R = (number // 10) + 1000 * number % 10

        if not DP[num_D]:
            DP[num_D] = string + "D"
            Queue.append((num_D, string + "D"))
        if not DP[num_S]:
            DP[num_S] = string + "S"
            Queue.append((num_S, string + "S"))
        if not DP[num_L]:
            DP[num_L] = string + "L"
            Queue.append((num_L, string + "L"))
        if not DP[num_R]:
            DP[num_R] = string + "R"
            Queue.append((num_R, string + "R"))

    print(DP[target])