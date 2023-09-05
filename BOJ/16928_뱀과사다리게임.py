from sys import stdin
from math import inf
from collections import deque

input = stdin.readline

ladder_cnt, snake_cnt = map(int, input().split())
board_map = [0] * 101
board_cnt = [inf] * 101

for i in range(ladder_cnt + snake_cnt):
    start, end = map(int, input().split())
    board_map[start] = end

Queue = deque([1])
board_cnt[1] = 0

while Queue:
    current = Queue.popleft()
    if current == 100:
        print(board_cnt[100])
        break
    move_cnt = board_cnt[current]

    for i in range(1, 7):
        if (next_ := current + i) <= 100 and board_cnt[next_] > move_cnt + 1:
            if special := board_map[next_]:
                board_cnt[next_] = move_cnt + 1 # next 방문처리 & 사다리 or 뱀으로 이동
                if board_cnt[special] > move_cnt + 1: # 여기서 방문 확인해줘야 함..
                    board_cnt[special] = move_cnt + 1
                    Queue.append(special)
            else:
                board_cnt[next_] = move_cnt + 1
                Queue.append(next_)