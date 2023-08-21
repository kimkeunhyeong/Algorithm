start, end = map(int, input().split())

# 짝수 제외, 추후 2 추가
# numbers[i] = 2*i + 1의 소수 여부 저장
numbers = [True] * ((end + 1)// 2)
numbers[0] = False # 1 제외

# 짝수는 모두 제외되었으므로, 3부터 sqrt(end)까지의 홀수를 검사
for i in range(3, int(end ** 0.5) + 1, 2):
    if numbers[i // 2]:
        # 시작지점이 i*2가 아닌 i*i 인 이유?
        # i * (1, 2, 3, ..., i) 중, i는 소수이고 짝수들은 모두 제거되었음.
        # 이후 홀수들은 모두 이전의 홀수 loop 검사때 제외되었으므로, 다시 검사할 필요가 없음.
        # -> i*i부터 i*2 배수만 지워주면 됨.
        numbers[i*i // 2::i] = [False] * ((end-i*i) // (2*i) + 1)
        # ((end-i*i -1) // (2*i) + 1) 로 써서 자꾸 ValueError 떴음.
        # sequence 할당시 갯수 확인 !!

if start <= 2:
    result = [2]
else:
    result = []

result += [2 * i + 1 for i in range(start // 2, (end + 1) // 2) if numbers[i]]
print(*result, sep="\n")