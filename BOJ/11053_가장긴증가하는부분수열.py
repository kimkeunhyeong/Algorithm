N = int(input())
data = list(map(int, input().split()))
array = [1] * N

for i in range(1, N):
    for j in range(i):
        if data[j] < data[i]:
            array[i] = max(array[i], array[j] + 1)

print(max(array))