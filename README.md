# Sorting Benchmark Lab

Mini project for CS314 *Divide and Conquer*. It compares **insertion sort**, **merge sort** and
**Python's built-in `sorted()`** on sorted, reversed and random data, for n = 10^3 up to 10^6.

## Files
| File | What it is |
|---|---|
| `sorts.py` | The algorithms (insertion sort, merge sort, `sorted()` wrapper) |
| `test_sorts.py` | 14 unit tests |
| `benchmark.py` | Runs the experiments, writes `results.csv` and the plots |
| `results.csv` | Raw timings |
| `benchmark_plot.png`, `speedup_plot.png` | Figures |
| `report.pdf` | 2-page report |
| `reflection.md` | What surprised me and what I would do next |
| `DEMO.md` | Script for the 5-minute demo |

## How to run
```
pip install matplotlib
python -m unittest -v      # run the tests
python benchmark.py        # run the experiments (about 1 minute)
```

## Key results
| n = 10,000 | Insertion | Merge | `sorted()` |
|---|---|---|---|
| sorted | 1.64 ms | 30.1 ms | 0.09 ms |
| reversed | 3.74 s | 14.4 ms | 0.08 ms |
| random | 1.70 s | 18.2 ms | 1.23 ms |

At n = 1,000,000 (insertion sort skipped, it would take hours): merge sort needs 4.46 s on random data,
`sorted()` needs 0.36 s.

## Notes
- Insertion sort is only measured up to n = 10,000 because it is O(n^2).
- Times depend on the machine, but the shape of the curves does not.
- Random data uses a fixed seed (42), and every result is checked against `sorted()`.
