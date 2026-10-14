import random
import timeit
import matplotlib.pyplot as plt

from merge_sort import merge_sort
from insertion_sort import insertion_sort

k = 100
n = 500

results = {}

for i in range(1, n + 1):
    total_insertion = 0.0
    total_merge = 0.0

    for _ in range(k):
        unsorted = [random.randint(-1000, 1000) for _ in range(i)]
        unsorted_copy = unsorted.copy()

        total_insertion += timeit.timeit("insertion_sort(unsorted)", globals=globals(), number=1)
        total_merge += timeit.timeit("merge_sort(unsorted_copy)", globals=globals(), number=1)

    results[("insertion", i)] = total_insertion / k
    results[("merge", i)] = total_merge / k

sizes = list(range(1, n + 1))
plt.figure()
plt.plot(sizes, [results[("insertion", s)] for s in sizes], label="Insertion Sort")
plt.plot(sizes, [results[("merge", s)] for s in sizes], label="Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.savefig("plot.png", dpi=300)

zoom_sizes = list(range(1, 121))
plt.figure()
plt.plot(zoom_sizes, [results[("insertion", s)] for s in zoom_sizes], label="Insertion Sort")
plt.plot(zoom_sizes, [results[("merge", s)] for s in zoom_sizes], label="Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Performance, crossover point")
plt.legend()
plt.savefig("crossover_plot.png", dpi=300)
plt.show()
