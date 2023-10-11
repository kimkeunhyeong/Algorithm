from sys import stdin

input = stdin.readline

str_A = " " + input().rstrip() # len_A/B 간소화 및 index_err 방지용
str_B = " " + input().rstrip()
len_A = len(str_A)
len_B = len(str_B)
array = [[0] * (len_B) for i in range(len_A)]

for i in range(1, len_A):
    for j in range(1, len_B):
        if str_A[i] == str_B[j]:
            # 값이 같은 경우, 지금까지의 최대 공통 길이 + 1로 설정해줌.
            # i, j에서 일치했으므로 두 문자열 모두 한글자씩 줄어든 위치인 i-1, j-1을 참조함.
            array[i][j] = array[i - 1][j - 1] + 1
        else:
            # 값이 같지 않은 경우, str_A[i - 1]와 str_B[j]까지 혹은 str_B[j - 1]와 str_A[i]를 비교한 것 중 더 큰 것을 선택함.
            # -> str_A나 str_B에서 한글자를 버렸을 때, 더 많이 겹치는 쪽을 선택하는 것.
            array[i][j] = max(array[i - 1][j], array[i][j - 1])

print(array[len_A - 1][len_B - 1])