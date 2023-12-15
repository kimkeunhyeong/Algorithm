from sys import stdin
from collections import deque

input = stdin.readline
num_people, num_party = map(int, input().split())
data = [set() for i in range(num_people + 1)]

truth = list(map(int, input().split()))
party = []

for i in range(num_party):
    party.append(set(list(map(int, input().split()))[1:]))
    update_data = set(party[-1])
    for info in party[-1]:
        data[info].update(update_data)

for i in range(1, num_people + 1):
    data[i].discard(i)

if truth[0] == 0:
    print(num_party)
else:
    Queue = deque(truth[1:])
    truth_member = set(truth[1:])
    Visited = [False] * (num_people + 1)

    while Queue:
        check = Queue.popleft()

        for i in data[check]:
            if i not in truth_member:
                Queue.append(i)
                truth_member.add(i)
    result = 0
    for check in party:
        if not len(truth_member.intersection(check)):
            result += 1
    
    print(result)