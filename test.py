import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy
from time import perf_counter

def baseline_max_sublist(list):
    max_sum = float('-inf')
    best_sublist = []

    for start in range(len(list)):
        current_sum = 0
        current_sublist = []

        for index in range(start, len(list)):
            current_sum += list[index]
            current_sublist.append(list[index])

            if current_sum > max_sum:
                max_sum = current_sum
                best_sublist = current_sublist.copy()

    return best_sublist, max_sum

from ast import If

def kadane_max_sublist(arr):
    max_so_far = float('-inf')
    current_max = 0
    for i in range(0, len(arr) - 1):
        current_max = current_max + arr[i]
        if current_max > max_so_far:
            max_so_far = current_max
        if current_max < 0:
            current_max = 0
    return max_so_far


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_max_sublist(arr))

def random_list(length, lower_bound=-100, upper_bound=100):
    list = numpy.random.randint(lower_bound, upper_bound, size=length)
    return list

lengths = [100,500,1000,2500,5000,10000]
baseline = []
kadane = []

for length in lengths:
    test_list = random_list(length)

    start = time.perf_counter()
    baseline_result = baseline_max_sublist(test_list)
    baseline_time = time.perf_counter() - start
    baseline.append(baseline_time)

    start = time.perf_counter()
    kadane_result = kadane_max_sublist(test_list)
    kadane_time = time.perf_counter() - start
    kadane.append(kadane_time)

plt.yscale('log')
plt.plot(lengths, baseline, marker='o', label='Baseline Times')
plt.plot(lengths, kadane, marker='o', label='Kadane Times')
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.title('Baseline vs Kadane Times')
plt.legend()
plt.show()