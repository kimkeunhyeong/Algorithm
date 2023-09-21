from sys import stdin

input = stdin.readline

things_cnt, max_weight = map(int, input().split())
things = []
for i in range(things_cnt):
    things.append(list(map(int, input().split())))

things = sorted(filter(lambda x : x[0] <= max_weight, things), key = lambda x : (x[0], x[1]), reverse = True)

DP = [0] * (max_weight + 1)

for weight, value in things:
    for i in range(max_weight, weight - 1, -1):
        DP[i] = max(DP[i], DP[i - weight] + value)
    
print(DP[-1])