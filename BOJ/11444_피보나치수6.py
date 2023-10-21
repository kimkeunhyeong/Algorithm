def get_exp(matrix, N):
    if N == 0:
        return [[1, 0], [0, 1]] # 단위행렬
    if N == 1:
        return matrix
    
    split_1 = get_exp(matrix, N // 2) # N이 짝수인 경우, 절반. 홀수인 경우 (N - 1)의 절반
    split_2 = N % 2

    half = mat_mul(split_1, split_1) # (N // 2) * 2
    if split_2:
        return mat_mul(half, matrix) # 홀수인 경우 1회 더 진행
    else:
        return half

def mat_mul(matrix_A, matrix_B):
    # A x B -> A의 col과 B의 row가 일치해야함.
    # -> return : [A_row x B_col] matrix
    row_A = len(matrix_A)
    col_B = len(matrix_B[0])

    result = [[] for i in range(row_A)]
    for i in range(row_A):
        for j in range(col_B):
            result[i].append(sum(map(lambda x : x[0] * x[1], zip(matrix_A[i], matrix_B[j]))) % mod)

    return result

N = int(input())
mod = 1_000_000_007

matrix = [[1, 1], [1, 0]]

print(mat_mul(get_exp(matrix, N), [[1], [0]])[1][0])