from collections import deque

start, target = map(int, input().split())
if start == target:
    print(0, 1, sep = "\n")
elif start > target:
    print(start - target, 1, sep = "\n")
else:
    count = 0
    Visited = [0] * 100_001
    Queue = deque()
    Queue.append((start, 0))
    Visited[start] = 1
    while Queue:
        point, step = Queue.popleft()
        next_step = step + 1
        for i in [point * 2, point - 1, point + 1]:
            if i == point:
               continue
            if 0 <= i <= 100_000 and (not Visited[i] or Visited[i] == next_step):
                Visited[i] = next_step
                if i == target:
                    count += 1
                else:
                    Queue.append((i, next_step))

    print(Visited[target], count, sep = "\n")