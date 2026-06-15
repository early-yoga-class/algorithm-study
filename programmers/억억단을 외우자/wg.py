def solution(e, starts):
    divisor_counts = [0] * (e + 1)

    for divisor in range(1, e + 1):
        for multiple in range(divisor, e + 1, divisor):
            divisor_counts[multiple] += 1

    best_numbers = [0] * (e + 2)
    best_numbers[e] = e

    for number in range(e - 1, 0, -1):
        current_best = best_numbers[number + 1]
        if divisor_counts[number] >= divisor_counts[current_best]:
            best_numbers[number] = number
        else:
            best_numbers[number] = current_best

    return [best_numbers[start] for start in starts]
