from sys import stdin
from collections import deque

def BFS():
    Visited = [0] * (N + 1)
    Queue = deque([1])
    Visited[1] = 1

    while Queue:
        node = Queue.popleft()
        for new_node in Tree[node]:
            if not Visited[new_node]:
                Queue.append(new_node)
                Visited[new_node] = node
    return Visited[2:]

input = stdin.readline

N = int(input())
Tree = [[] for i in range(N+1)]
for i in range(N-1):
    A, B = map(int, input().split())
    Tree[A].append(B)
    Tree[B].append(A)

print(*BFS(), sep = "\n")