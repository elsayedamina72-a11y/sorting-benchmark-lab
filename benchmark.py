"""Sorting Benchmark Lab: compare insertion sort, merge sort and Python's sorted().

Run:  python benchmark.py
Outputs: results.csv, benchmark_plot.png, speedup_plot.png
"""
import csv
import random
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sorts import insertion_sort, merge_sort, python_sorted

SIZES = [1_000, 3_000, 10_000, 30_000, 100_000, 300_000, 1_000_000]
INPUT_TYPES = ["sorted", "reversed", "random"]
ALGORITHMS = {
    "insertion": insertion_sort,
    "merge": merge_sort,
    "python sorted()": python_sorted,
}
# Insertion sort is O(n^2): at n = 10^6 it would take hours in pure Python,
# so it is only measured up to this size and extrapolated beyond it.
INSERTION_MAX_N = 10_000

random.seed(42)


def make_input(kind, n):
    if kind == "sorted":
        return list(range(n))
    if kind == "reversed":
        return list(range(n, 0, -1))
    return [random.randint(0, 10 * n) for _ in range(n)]


def time_it(fn, data):
    """Best of several runs (fewer runs for big inputs) in seconds."""
    runs = 3 if len(data) <= 10_000 else 1
    best = float("inf")
    for _ in range(runs):
        start = time.perf_counter()
        result = fn(data)
        best = min(best, time.perf_counter() - start)
    assert result == sorted(data), f"{fn.__name__} gave a wrong result"
    return best


rows = []
print(f"{'input':<10}{'n':>10}{'insertion(s)':>16}{'merge(s)':>12}{'sorted()(s)':>14}")
for kind in INPUT_TYPES:
    for n in SIZES:
        data = make_input(kind, n)
        line = {}
        for name, fn in ALGORITHMS.items():
            if name == "insertion" and n > INSERTION_MAX_N:
                line[name] = None
                continue
            line[name] = time_it(fn, data)
            rows.append({"input": kind, "n": n, "algorithm": name, "seconds": line[name]})
        ins = f"{line['insertion']:.4f}" if line["insertion"] is not None else "skipped"
        print(f"{kind:<10}{n:>10}{ins:>16}{line['merge']:>12.4f}{line['python sorted()']:>14.4f}")

with open("results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["input", "n", "algorithm", "seconds"])
    writer.writeheader()
    writer.writerows(rows)


def series(kind, algo):
    pts = [(r["n"], r["seconds"]) for r in rows if r["input"] == kind and r["algorithm"] == algo]
    return [p[0] for p in pts], [p[1] for p in pts]


# Plot 1: time vs n for each input type (log-log)
colors = {"insertion": "red", "merge": "orange", "python sorted()": "green"}
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=True)
for ax, kind in zip(axes, INPUT_TYPES):
    for algo in ALGORITHMS:
        xs, ys = series(kind, algo)
        ax.plot(xs, ys, marker="o", label=algo, color=colors[algo])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(f"{kind} input")
    ax.set_xlabel("n")
    ax.grid(True, which="both", alpha=0.3)
axes[0].set_ylabel("time (seconds, log scale)")
axes[0].legend()
plt.suptitle("Sorting benchmark: running time vs input size")
plt.tight_layout()
plt.savefig("benchmark_plot.png", dpi=150)
plt.close()

# Plot 2: how much faster is sorted() than merge sort?
plt.figure(figsize=(7, 4.5))
for kind in INPUT_TYPES:
    xs, merge_t = series(kind, "merge")
    _, py_t = series(kind, "python sorted()")
    plt.plot(xs, [m / p for m, p in zip(merge_t, py_t)], marker="o", label=kind)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("merge sort time / sorted() time")
plt.title("How many times faster is Python's sorted()?")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.savefig("speedup_plot.png", dpi=150)
plt.close()

print("\nSaved results.csv, benchmark_plot.png, speedup_plot.png")
