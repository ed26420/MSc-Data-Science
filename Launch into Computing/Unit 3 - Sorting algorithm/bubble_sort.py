import pandas as pd
import time


data = pd.read_csv('winequality-white.csv', sep=';')
alcohol_values = data['alcohol'].tolist()

def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def quick_sort(numbers):

    # A list with 0 or 1 item is already sorted
    if len(numbers) <= 1:
        return numbers

    # Choose the middle value as the pivot
    pivot = numbers[len(numbers) // 2]

    # Values smaller than the pivot
    left = [x for x in numbers if x < pivot]

    # Values equal to the pivot
    middle = [x for x in numbers if x == pivot]

    # Values greater than the pivot
    right = [x for x in numbers if x > pivot]

    # Sort left and right, then combine everything
    return quick_sort(left) + middle + quick_sort(right)


# Different input sizes
sizes = [100, 500, 1000, 2000, 4000]

print("Bubble Sort:")

for size in sizes:
    sample = alcohol_values[:size].copy()

    start_time = time.perf_counter()

    bubble_sort(sample)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(size, "values:", elapsed_time, "seconds")


print("\nQuicksort:")

for size in sizes:
    sample = alcohol_values[:size].copy()

    start_time = time.perf_counter()

    quick_sort(sample)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(size, "values:", elapsed_time, "seconds")