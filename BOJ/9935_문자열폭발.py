from sys import stdin
input = stdin.readline

string = input().rstrip()
bomb_string = input().rstrip()
bomb_check = bomb_string[:-1]
bomb_len = len(bomb_string)
check_len = len(bomb_check)
stack = []
index = 0

while index < len(string):
    for i in range(bomb_len):
        if string[index + i] != bomb_string[i]:
            break
    else:
        index += bomb_len
        continue
    if string[index] == bomb_string[-1]:
        if stack[-check_len:] == list(bomb_check):
            for i in range(check_len):
                stack.pop()
            index += 1
            continue
    stack.append(string[index])
    index += 1

if stack:
    print("".join(stack))
else:
    print("FRULA")