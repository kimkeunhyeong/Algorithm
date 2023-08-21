from sys import stdin
input = stdin.readline

n = int(input())
stack = []
next_push_value = 1
operations = []
while next_push_value <= n or stack:
    target_value = int(input())
    while target_value >= next_push_value:
        stack.append(next_push_value)
        operations.append("+")
        next_push_value += 1
    if stack[-1] == target_value:
        stack.pop()
        operations.append("-")
    else:
        operations = None
        break

if operations:
    print(*operations, sep="\n")
else:
    print("NO")