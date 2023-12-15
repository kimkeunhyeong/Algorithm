def is_promising(depth:int):
    for check in range(depth):
        # 서로 다른 column의 값이 같은 경우, 동일한 row에 2개가 존재. 뒷부분은 대각선 체크
        if column[check] == column[depth] or abs(column[check] - column[depth]) == depth - check:
            return False
    return True

def NQueen(depth:int):
    global result
    if depth == N:
        result += 1
        return
    else:
        for i in range(N):
            # Visited로 이미 검사 끝난 항목을 제외하지 않으면 시간초과 발생
            if Visited[i]:
                continue
            
            column[depth] = i
            if is_promising(depth):
                Visited[i] = True
                NQueen(depth + 1)
                Visited[i] = False

N = int(input())
result = 0
# 일단, 한 줄당 하나만 존재할 수 있음 -> row or col만 검사하면 됨.
column = [0] * N
Visited = [False] * N
NQueen(0)
print(result)