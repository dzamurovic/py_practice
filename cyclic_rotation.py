def solution(A, K):
    if len(A) == 0:
        return []

    K %= len(A)

    if K == 0:
        return A

    return A[-K:] + A[:-K]

a = [1,2,3]
print solution(a, 1)