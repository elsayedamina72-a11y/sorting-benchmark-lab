# 5-minute demo script

**0:00 - Goal (30 s).** "I compared insertion sort, merge sort and Python's sorted() on sorted, reversed and random data from 1,000 to 1,000,000 elements."

**0:30 - Code (1 min).** Open `sorts.py`. Show insertion sort (shifting loop) and merge sort (split, sort, merge). Mention that results are checked against `sorted()`.

**1:30 - Tests (30 s).** In the terminal run `python -m unittest -v`. Point out the 14 passing tests.

**2:00 - Experiment (1 min).** Run `python benchmark.py`. While it runs, explain why insertion sort stops at n = 10,000 (quadratic, would take hours).

**3:00 - Plot (1 min 30 s).** Open `benchmark_plot.png`. Say: insertion sort is the steepest line, merge sort is much flatter, sorted() is lowest. On sorted input, insertion sort beats merge sort.

**4:30 - Conclusion (30 s).** Use insertion sort for small or nearly sorted data, merge sort for big general data, and the library sort in practice. Next step: the hybrid sort.

Tip: record the screen with the phone or laptop screen recorder while you follow these steps.
