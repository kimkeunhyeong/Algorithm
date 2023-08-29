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

def DFS(y, x, depth, value):
    global result
    if result > value + max_value * (4 - depth): # 이 조건으로 가지치기 안하면 오히려 2배걸림..
        return
    
    if depth == 4:
        result = max(result, value)
        return
    
    for next_y, next_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if 0 <= next_y < height and 0 <= next_x < width and not Visited[next_y][next_x]:
            Visited[next_y][next_x] = True
            DFS(next_y, next_x, depth + 1, value + num_data[next_y][next_x])
            Visited[next_y][next_x] = False

input = stdin.readline

height, width = map(int, input().split())

num_data = [list(map(int, input().split())) for i in range(height)]
max_value = result = 0

for i in num_data:
    max_value = max(max_value, max(i))

""" for i in range(height): # 세로
    for j in range(width): # 가로
        result = max(result, get_score(i, j))
"""

Visited = [[False] * width for _ in range(height)]

for i in range(height):
    for j in range(width):
        Visited[i][j] = True
        DFS(i, j, 1, num_data[i][j])
        Visited[i][j] = False

        if i + 2 < height:
            type_LT_common_H = sum(num_data[i + value][j] for value in range(3))
            type_LT_sub_H = [(i + 1, j - 1), (i + 1, j + 1)]
            for y, x in type_LT_sub_H:
                if 0 <= x < width:
                    result = max(result, type_LT_common_H + num_data[y][x])
        if j + 2 < width:
            type_LT_common_V = sum(num_data[i][j + value] for value in range(3))
            type_LT_sub_V = [(i + 1, j + 1), (i - 1, j + 1)]
            for y, x in type_LT_sub_V:
                if 0 <= y < height:
                    result = max(result, type_LT_common_V + num_data[y][x])

print(result)