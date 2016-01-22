def solution(A):
    result = A[0]
    for i in range(1, len(A)):
        result ^= A[i]
    return result