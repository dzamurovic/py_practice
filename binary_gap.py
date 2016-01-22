def binary_gap(N):
    # write your code in Python 2.7
    binary = bin(N)[2:]

    max_gap = 0
    current_gap = 0

    while len(binary) > 0 and binary[len(binary) - 1] == '0':
        binary = binary[:len(binary) - 1]

    start = 0
    while start < len(binary):
        if binary[start] == '0':
            break;
        start += 1

    for i in range (start, len(binary)):
        if binary[i] == '0':
            current_gap += 1
        else:
            if current_gap != 0:
                max_gap = max(max_gap, current_gap)
                current_gap = 0

    return max_gap

print binary_gap(1012)