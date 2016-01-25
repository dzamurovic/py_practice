def solution(A):
    n = max(A)
    sum1 = (n / 2) * (n + 1) + (n - n / 2)

    sum2 = 0
    for a in A:
        sum2 += a

    return sum1 - sum2