import sys

n= int(sys.stdin.readline().rstrip())

def matrix_multiply(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k]%1000000007 * B[k][j]%1000000007
    return result

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        return matrix_power(matrix_multiply(matrix, matrix), n // 2)
    else:
        return matrix_multiply(matrix, matrix_power(matrix_multiply(matrix, matrix), (n - 1) // 2))

def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n-1)
    return result_matrix[0][0]

a=fibonacci(n)
print(a%1000000007)