import time


def my_solution(arr):
    res = []
    sortedArr = sorted(arr, reverse=True)

    if len(sortedArr) == 0:
        return res

    res.append(sortedArr[0])
    tmp = sortedArr[0]

    for i in sortedArr:
        if i != tmp:
            res.append(i)
            tmp = i

    return res


def solution(arr):
    res = list(set(arr))
    res.sort(reverse=True)
    return res


def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    print("Time:  ", format(end_time - start_time, "0.10f"))
    print("Result:", result)


sample = [1, 1, 2, 2, 2, 3, 3]
measure_time(my_solution, sample)

sample = [1, 1, 2, 2, 2, 3, 3]
measure_time(solution, sample)
