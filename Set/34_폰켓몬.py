def solution(nums):
    max_count = len(nums) / 2
    _set = set(nums)
    print(_set)
    min_count = len(_set)
    return min(int(max_count), int(min_count))


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
