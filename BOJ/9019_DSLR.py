from sys import stdin
from collections import deque

input = stdin.readline
TC = int(input())

for _ in range(TC):
    current, target = map(int, input().rstrip().split())
    
    DP = [-1] * 10000

    Queue = deque([current])
    DP[current] = ""

    while Queue:
        number = Queue.popleft()
        # pypy3 기준 (number, string) tuple 입력 -> number 단일로 변경시
        # 8468ms -> 5584ms로 시간이 34% 줄어듦.
        if number == target:
            break

        num_D = (number * 2) % 10000
        num_S = number - 1 if number > 0 else 9999
        num_L = (number % 1000) * 10 + number // 1000
        num_R = (number // 10) + 1000 * (number % 10) # 이런... 함수 제거한 다음 옮기면서 괄호를 안 씌웠었다..

        if DP[num_D] == -1:
            DP[num_D] = DP[number] + "D"
            Queue.append(num_D)
        if DP[num_S] == -1:
            DP[num_S] = DP[number] + "S"
            Queue.append(num_S)
        if DP[num_L] == -1:
            DP[num_L] = DP[number] + "L"
            Queue.append(num_L)
        if DP[num_R] == -1:
            DP[num_R] = DP[number] + "R"
            Queue.append(num_R)

    print(DP[target])