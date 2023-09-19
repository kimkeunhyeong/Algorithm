from collections import deque

def BFS(start, target):
    Queue = deque()
    Visited = [-1] * 100001
    Queue.append(start)
    Visited[start] = 0

    while Queue:
        check = Queue.popleft()
        curr_time = Visited[check] + 1
        if check == target:
            break

        # Visited == False로 검사한 부분에서, 최초 시작점의 방문처리가 불가능해서 오류 발생함.
        # -> 시작값을 0이 아닌 -1로 설정하여 방문여부를 확인
        if check < 50001 and Visited[check * 2] == -1:
            Visited[check * 2] = Visited[check]
            Queue.append(check * 2)
        if check > 0 and Visited[check - 1] == -1:
            Visited[check - 1] = curr_time
            Queue.append(check - 1)
        if check < 100000 and Visited[check + 1] == -1:
            Visited[check + 1] = curr_time
            Queue.append(check + 1)

    print(Visited[target])

start, target = map(int, input().split())

if start >= target:
    print(abs(target - start))
else:
    BFS(start, target)