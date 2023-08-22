from sys import stdin

def check_square(y, x, size):
    global white_cnt
    global blue_cnt

    initial_color = color_data[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if color_data[i][j] != initial_color:
                check_square(y, x, size // 2)
                check_square(y + size // 2, x, size // 2)
                check_square(y, x + size // 2, size // 2)
                check_square(y + size // 2, x + size // 2, size // 2)
                break
        else:
            continue
        break
    else:
        if initial_color == "0":
            white_cnt += 1
        else:
            blue_cnt += 1

input = stdin.readline

N = int(input())

color_data = []
for i in range(N):
    color_data.append(list(input().rstrip().split()))

white_cnt = blue_cnt = 0

check_square(0, 0, N)

print(white_cnt, blue_cnt, sep = "\n")