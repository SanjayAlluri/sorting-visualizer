# sorting_algorithms.py

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    operations = 0

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                operations += 1
                swapped = True

                yield arr.copy(), comparisons, operations

        if not swapped:
            break

    yield arr.copy(), comparisons, operations


def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    operations = 0

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            operations += 1

            yield arr.copy(), comparisons, operations

    yield arr.copy(), comparisons, operations


def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    operations = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                operations += 1
                yield arr.copy(), comparisons, operations
                j -= 1
            else:
                break

        arr[j + 1] = key
        operations += 1

        yield arr.copy(), comparisons, operations

    yield arr.copy(), comparisons, operations


def merge_sort(arr):
    comparisons = 0
    operations = 0

    def merge(left, mid, right):
        nonlocal comparisons, operations

        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]

        i = 0
        j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            comparisons += 1

            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1

            operations += 1
            k += 1

            yield arr.copy(), comparisons, operations

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            operations += 1

            yield arr.copy(), comparisons, operations

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            operations += 1

            yield arr.copy(), comparisons, operations

    def divide(left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        yield from divide(left, mid)
        yield from divide(mid + 1, right)
        yield from merge(left, mid, right)

    if len(arr) > 1:
        yield from divide(0, len(arr) - 1)

    yield arr.copy(), comparisons, operations


ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
}

COMPLEXITIES = {
    "Bubble Sort": {
        "Best": "O(n)",
        "Average": "O(n²)",
        "Worst": "O(n²)",
        "Space": "O(1)",
    },
    "Selection Sort": {
        "Best": "O(n²)",
        "Average": "O(n²)",
        "Worst": "O(n²)",
        "Space": "O(1)",
    },
    "Insertion Sort": {
        "Best": "O(n)",
        "Average": "O(n²)",
        "Worst": "O(n²)",
        "Space": "O(1)",
    },
    "Merge Sort": {
        "Best": "O(n log n)",
        "Average": "O(n log n)",
        "Worst": "O(n log n)",
        "Space": "O(n)",
    },
}
