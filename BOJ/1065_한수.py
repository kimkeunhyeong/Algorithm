N = int(input())

if N <= 99: # 공차가 0인 경우도 등차수열이므로 모든 수가 해당
    print(N)
else:
    count = 99
    if N == 1000: # 1000 예외처리
        N = 999
    for i in range(101, N + 1):
        one, two, three = i // 100, (i // 10) % 10, i % 10
        if three - two == two - one:
            count += 1
    print(count)