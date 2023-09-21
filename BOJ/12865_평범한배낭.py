from sys import stdin

input = stdin.readline

things_cnt, max_weight = map(int, input().split())
things = []
for i in range(things_cnt):
    things.append(list(map(int, input().split())))

DP = [0] * (max_weight + 1)

for i in things:
    if i[0] <= max_weight and DP[i[0]] < i[1]:
        DP[i[0]] = i[1]
        for j in range(i[0], max_weight + 1):
            DP[j] = max(DP[j], DP[j - i[0]] + i[1])
            
print(DP[-1])