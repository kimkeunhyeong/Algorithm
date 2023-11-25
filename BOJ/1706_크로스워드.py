from sys import stdin

input = stdin.readline

height, width = map(int, input().split())
data = [input().rstrip() for i in range(height)]
rotated_data = list(map("".join, zip(*data))) # zip을 이용, 회전시켜줌

words = []

for Y in range(height): # 원본, 가로 탐색
    for i in data[Y].split("#"):
        if len(i) > 1:
            words.append(i)
for X in range(width): # 회전본, 세로 탐색
    for i in rotated_data[X].split("#"):
        if len(i) > 1:
            words.append(i)

print(sorted(words)[0])