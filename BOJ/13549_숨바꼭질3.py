from collections import deque

def BFS(start, target):
    Queue = deque()
    Visited = [0] * 100001
    Queue.append(start)

    while Queue:
        check = Queue.popleft()
        curr_time = Visited[check] + 1
        if check == target:
            break

        if check < 50001 and not Visited[check * 2]:
            Visited[check * 2] = curr_time - 1
            Queue.append(check * 2)
        if check > 0 and not Visited[check - 1]:
            Visited[check - 1] = curr_time
            Queue.append(check - 1)
        if check < 100000 and not Visited[check + 1]:
            Visited[check + 1] = curr_time
            Queue.append(check + 1)

    print(Visited[target])

start, target = map(int, input().split())

if start >= target:
    print(abs(target - start))
else:
    BFS(start, target)