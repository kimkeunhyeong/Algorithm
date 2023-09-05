from sys import stdin

input = stdin.readline

ladder_cnt, snake_cnt = map(int, input().split())
board_map = [i for i in range(101)]
board_cnt = [0] * 101

for i in range(ladder_cnt + snake_cnt):
    start, end = map(int, input().split())
    board_map[start] = end

Queue = [1]

while Queue:
    current = Queue.pop(0)
    # O(N)에서 N이 충분히 작은 경우, deque보다 list.pop(0)이 빠를 수도 있음.
    move_cnt = board_cnt[current] + 1
    start = current + 1
    end = current + 7 if current <= 94 else 101 # 범위 검사는 한번만 하도록 변경

    for i in range(start, end):
        next_ = board_map[i] # 사다리 or 뱀인 경우 해당 칸으로 이동하고
        if not board_cnt[next_]:
            board_cnt[next_] = move_cnt # 방문처리
            Queue.append(next_)

print(board_cnt[100])