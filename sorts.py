"""Sorting algorithms used in the Sorting Benchmark Lab."""


def insertion_sort(arr):
    """Return a sorted copy of arr using insertion sort. O(n^2) worst case, O(n) best case."""
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def insertion_sort_counts(arr):
    """Insertion sort that also returns (sorted_list, comparisons, shifts)."""
    a = list(arr)
    comparisons = 0
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comparisons, shifts


def merge(left, right):
    """Merge two sorted lists into one sorted list (stable)."""
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def merge_sort(arr):
    """Return a sorted copy of arr using top-down merge sort. O(n log n) in all cases."""
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def python_sorted(arr):
    """Python's built-in sorted() (Timsort, a hybrid of merge sort and insertion sort)."""
    return sorted(arr)
