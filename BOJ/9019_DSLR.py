from sys import stdin
from collections import deque

def operation(number : int, op_type : str) -> int:
    match op_type:
        case "D":
            return (number * 2) % 10000
        case "S":
            return number - 1 if number > 0 else 9999
        case "L":
            digit_one = number // 1000
            return (number % 1000) * 10 + digit_one
        case "R":
            digit_four = number % 10
            return (number // 10) + 1000 * digit_four
        case _:
            raise TypeError
        
input = stdin.readline
TC = int(input())

for _ in range(TC):
    current, target = map(int, input().rstrip().split())
    
    DP = [False] * 10000

    Queue = deque([(current, "")])
    
    while Queue:
        number, string = Queue.popleft()
        current_length = len(string)

        for op in ["D", "S", "L", "R"]:
            next_number = operation(number, op)
            if not DP[next_number]:
                DP[next_number] = string + op
                Queue.append((next_number, string + op))

    print(DP[target])