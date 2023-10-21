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
        # 순서를 신경써줘야 했던 이유 : 증가하는 방향인 경우, 참조해야 하는 값이 이전 loop에 의해 변경되므로,
        # 뒤에서부터 확인을 해야 문제가 발생하지 않음.
        DP[i] = max(DP[i], DP[i - weight] + value)
    
print(DP[-1])