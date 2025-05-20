import time


def sort_array_ascending(arr):
    res = sorted(arr)
    return res


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr


def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    print(end_time - start_time, result)
    return end_time - start_time, result


# O(N^2)
arr = list(range(10000))
bubble_time, bubble_res = measure_time(bubble_sort, arr)
print("Bubble:", format(bubble_time, "0.10f"))

# O(NlogN)
arr = list(range(10000))
sorted_time, sorted_res = measure_time(sort_array_ascending, arr)
print("Sorted:", format(sorted_time, "0.10f"))
