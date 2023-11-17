from sys import stdin

def square(Y, X):
    size = search_size = 1
    check_char = map_data[Y][X]

    while Y + search_size < height and X + search_size < width:
        if map_data[Y + search_size][X + search_size] == check_char \
            and map_data[Y + search_size][X] == check_char \
            and map_data[Y][X + search_size] == check_char:
            size = search_size + 1
        search_size += 1
    return size

input = stdin.readline
height, width = map(int, input().split())
map_data = []
for i in range(height):
    map_data.append(input().rstrip())

if height == 1 or width == 1:
    print(1)
else:
    max_size = max(height, width)
    size = 1
    for i in range(height):
        for j in range(width):
            size = max(size, square(i, j))
            # 이 부분 이후 size가 남은 width or height보다 크면 검사 skip해서 시간 줄일 수 있을 듯
            if size == max_size:
                break
        else:
            continue # max_size보다 작은 경우 계속 탐색
        break # max_size인 경우 종료
    print(size**2)