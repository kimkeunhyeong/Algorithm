from sys import stdin

def get_score(i : int, j : int) -> list:
    """
    get score by bruteforce
    """
    # type I
    result = 0
    type_IO = []
    if i + 3 < height:
        type_IO.append(sum(num_data[i + value][j] for value in range(4)))
    if j + 3 < width:
        type_IO.append(sum(num_data[i][j + value] for value in range(4)))
    # type O
    if i + 1 < height and j + 1 < width:
        temp = 0
        for y, x in [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]:
            temp += num_data[y][x]
        type_IO.append(temp)

    if type_IO:
        result = max(type_IO)

    # type L, T
    if i + 2 < height:
        type_LT_common_H = sum(num_data[i + value][j] for value in range(3))
        type_LT_sub_H = [(i + value1, j + value2) for value1 in range(3) for value2 in range(-1, 2, 2)]
        for y, x in type_LT_sub_H:
            if 0 <= x < width:
                result = max(result, type_LT_common_H + num_data[y][x])
    if j + 2 < width:
        type_LT_common_V = sum(num_data[i][j + value] for value in range(3))
        type_LT_sub_V = [(i + value1, j + value2) for value2 in range(3) for value1 in range(-1, 2, 2)]
        for y, x in type_LT_sub_V:
            if 0 <= y < height:
                result = max(result, type_LT_common_V + num_data[y][x])
    # type S
    if i + 2 < height and j + 1 < width:
        type_S_common_H = num_data[i + 1][j] + num_data[i + 1][j + 1]
        type_S_sub_H = [(i, j), (i + 2, j + 1), (i, j + 1), (i + 2, j)]
        num = []
        for y, x in type_S_sub_H:
            num.append(num_data[y][x])
        result = max(result, type_S_common_H + max(sum(num[:2]), sum(num[2:])))
    if j + 2 < width and i + 1 < height:
        type_S_common_V = num_data[i][j + 1] + num_data[i + 1][j + 1]
        type_S_sub_V = [(i, j), (i + 1, j + 2), (i + 1, j), (i, j + 2)]
        num = []
        for y, x in type_S_sub_V:
            num.append(num_data[y][x])
        result = max(result, type_S_common_V + max(sum(num[:2]), sum(num[2:])))

    return result

input = stdin.readline

height, width = map(int, input().split())

num_data = [list(map(int, input().split())) for i in range(height)]

result = 0

for i in range(height): # 세로
    for j in range(width): # 가로
        result = max(result, get_score(i, j))

print(result)