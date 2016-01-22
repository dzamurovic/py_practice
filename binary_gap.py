def binary_gap(N):
    while N > 0 and N % 2 == 0:
        N //= 2

    current_gap = 0
    max_gap = 0
    while N > 0:
        if N % 2 == 0:
            current_gap += 1
        else:
            if current_gap > 0:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
        N //= 2

    return max_gap