from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def print_star(N : int):
    if N == 3:
        return ["  *  ", " * * ", "*****"]
    next_N = N // 2
    data = print_star(next_N)
    result = []
    for i in data:
        result.append(" " * next_N + i + " " * next_N)
    for i in range(next_N):
        result.append(data[i] + " " + data[i])

    return result
N = int(input())

result = print_star(N)
for i in range(N):
    print(result[i] + "\n")