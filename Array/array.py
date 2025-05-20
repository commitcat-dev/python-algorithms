def printArr(arr):
    for i in arr:
        print(i)


arr = list(range(6))

arr2 = [x * x for x in arr]
# arr2 = arr.map { $0 * $0 }

count = len(arr)
# count = arr.count
print(count)
print(arr.index(0))

print(arr)
print(arr2)

array = [9, 4, 3, 1, 2, 7]
# print(array)
# array.sort()
# print(array)
# array.sort(reverse=True)
# print(array)


def sort_array_ascending(arr):
    """
    주어진 배열을 오름차순으로 정렬하여 반환하는 함수

    Parameters:
    arr (list): 정렬할 숫자들의 리스트

    Returns:
    list: 오름차순으로 정렬된 리스트
    """
    return sorted(arr)


res = sort_array_ascending(array)
print(res)
