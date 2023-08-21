N, target_y, target_x= map(int, input().split())

start = 0
square_size = 2 ** N

center = (2 ** (N - 1), 2 ** (N - 1))

while square_size > 1:
    square_size //= 2
    number_range = square_size ** 2
    if center[0] - square_size <= target_y < center[0]: # (1, 2번 사분면인 경우, 좌상단이 1사분면, 우하단이 4사분면)
        if center[1] - square_size <= target_x < center[1]: # 1사분면인 경우
            center = (center[0] * 2 - square_size, center[1] * 2 - square_size)
        else:
            start += number_range
            center = (center[0] * 2 - square_size, center[1] * 2 + square_size)
    else: # (3, 4번 사분면인 경우)
        if center[1] - square_size <= target_x < center[1]: # 3사분면인 경우
            start += number_range * 2
            center = (center[0] * 2 + square_size, center[1] * 2 - square_size)
        else:
            start += number_range * 3
            center = (center[0] * 2 + square_size, center[1] * 2 + square_size)
    center = (center[0] // 2, center[1] // 2)

print(start)