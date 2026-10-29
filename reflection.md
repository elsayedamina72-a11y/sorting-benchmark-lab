# Reflection

**What surprised me**
- On already sorted input, insertion sort beat merge sort (1.6 ms vs 30 ms at n = 10,000), even though merge sort has the better big-O. Big-O describes growth, not every case.
- Python's `sorted()` sorted one million already-sorted numbers in about 14 ms, 25 times faster than it sorted random ones. It detects runs that already exist.
- Merge sort written in Python was about 12 times slower than `sorted()` on random data. Part of that is C versus Python, not only the algorithm.

**What I would do next**
- Build the Hybrid Sort: make merge sort switch to insertion sort for small pieces and find the best cutoff size.
- Re-write merge sort so it does not copy slices at every level (one shared buffer), and measure how much faster it gets.
- Repeat the experiment in C++ to remove the interpreter overhead from the comparison.
