from sys import stdin

input = stdin.readline

tree_cnt, target_length = map(int, input().split())
tree = list(map(int, input().split()))

start = result = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in tree:
        if i > mid:
            temp += (i - mid)

    if temp < target_length: # 나무가 모자람.
        end = mid - 1
    else: # 나무 충족됨 -> 정답 가능성 O
        start = mid + 1
        result = max(result, mid)

print(result)