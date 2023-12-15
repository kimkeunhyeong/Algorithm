from collections import deque, defaultdict
A, B = map(int, input().split())
if A > B:
    print(-1)
else:
    # input이 10**9까지 들어올 수 있어 메모리 초과 발생
    # Visited = [False] * (B + 1)
    # Visited를 dictionary로 변경해서 방문 node만큼만 늘어나도록 변경
    Visited = defaultdict(int)
    Queue = deque()
    Queue.append((A, 1))
    while Queue:
        num, cnt = Queue.popleft()
        for i in [num * 2, num * 10 + 1]:
            if i <= B and not Visited[i]:
                Queue.append((i, cnt + 1))
                Visited[i] = cnt + 1
    print(Visited[B] if Visited[B] else -1)