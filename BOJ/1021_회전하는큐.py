from collections import deque
from sys import stdin

input = stdin.readline
Queue_size, pop_size = map(int, input().split())
pop_order = list(map(int, input().split()))[::-1]

Queue = deque(i for i in range(1, Queue_size + 1))
result = 0

while pop_order:
    if Queue[0] != pop_order[-1]:
        for i in range(1, len(Queue)):
            if Queue[i] == pop_order[-1]:
                result += i
                Queue.rotate(-i)
                break
            if Queue[-i] == pop_order[-1]:
                result += i
                Queue.rotate(i)
                break
    Queue.popleft()
    pop_order.pop()
    
print(result)