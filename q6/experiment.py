import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import random
import timeit
import matplotlib.pyplot as plt

from q5.insertion_sort import insertion_sort
from q5.merge_sort import merge_sort
from hybrid_sort import hybrid_sort

trials = 50
k_values = list(range(1, 250, 5))

for n in [250, 500, 750, 1000]:
    results = []

    for k in k_values:
        total_time = 0.0

        for _ in range(trials):
            unsorted = [random.randint(-1000, 1000) for _ in range(n)]
            total_time += timeit.timeit("hybrid_sort(unsorted, k)", globals=globals(), number=1)

        results.append(total_time / trials)

    plt.plot(k_values, results, label=f"Hybrid Sort (n={n})")

plt.xlabel("Threshold (k)")
plt.ylabel("Time (seconds)")
plt.title("Hybrid Sort Runtime vs. Threshold k")
plt.legend()
plt.tight_layout()
plt.savefig("hybrid_plot.png", dpi=300)
plt.show()
