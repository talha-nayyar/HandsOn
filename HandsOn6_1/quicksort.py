import random
import time

import matplotlib.pyplot as plt
import numpy as np


#Non-Random Pivot QuickSort
def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    while low < high:
        pivot_index = partition(arr, low, high)
        
        if pivot_index - low < high - pivot_index:
            quicksort(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            quicksort(arr, pivot_index + 1, high)
            high = pivot_index - 1

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


#Random Pivot QuickSort
def quicksort_random(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    while low < high:
        pivot_index = random_partition(arr, low, high)
        
        if pivot_index - low < high - pivot_index:
            quicksort_random(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            quicksort_random(arr, pivot_index + 1, high)
            high = pivot_index - 1

    return arr


def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)


# Function to benchmark sorting time
def benchmark_quicksort(func, arr):
    arr_copy = arr[:]
    start_time = time.time()
    func(arr_copy, 0, len(arr_copy) - 1)
    return time.time() - start_time


#inputs
sizes = [100, 500, 1000, 2000, 5000, 10000]

best_case_times = []
worst_case_times = []
average_case_times = []

for n in sizes:
    best_case_input = list(range(n))  # Already sorted (best case)
    worst_case_input = list(range(n, 0, -1))  # Reverse sorted (worst case)
    average_case_input = np.random.randint(0, n, n).tolist()  # Random elements (average case)

    best_case_times.append(benchmark_quicksort(quicksort, best_case_input))
    worst_case_times.append(benchmark_quicksort(quicksort, worst_case_input))
    average_case_times.append(benchmark_quicksort(quicksort, average_case_input))

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(sizes, best_case_times, marker='o', linestyle='-', label='Best Case')
plt.plot(sizes, worst_case_times, marker='o', linestyle='-', label='Worst Case')
plt.plot(sizes, average_case_times, marker='o', linestyle='-', label='Average Case')

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("QuickSort (Non-Random Pivot) Time Complexity Analysis")
plt.legend()
plt.grid()
plt.show()
