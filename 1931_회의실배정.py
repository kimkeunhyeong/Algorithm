from sys import stdin

input = stdin.readline

N = int(input())
timetable = []
for i in range(N):
    timetable.append(tuple(map(int, input().split())))

timetable.sort(key = lambda x : (x[1], x[0]))

last_end = None
conf_cnt = 0
for i in timetable:
    if last_end == None:
        last_end = i[1]
        conf_cnt += 1
    else:
        if i[0] >= last_end:
            last_end = i[1]
            conf_cnt += 1
print(conf_cnt)