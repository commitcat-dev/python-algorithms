sample_1 = [2, 1, 3, 4, 1]
result_1 = [2, 3, 4, 5, 6, 7]

sample_2 = [5, 0, 2, 7]
result_2 = [2, 5, 7, 9, 12]


def my_solution(arr):
    n = len(arr)
    sum_list = []
    for i in range(n):
        for j in range(i + 1, n):
            print(arr[i], arr[j])
            sum_list.append(arr[i] + arr[j])
    return list(set(sum_list))


res = my_solution(sample_1)
print(res)

res = my_solution(sample_2)
print(res)
