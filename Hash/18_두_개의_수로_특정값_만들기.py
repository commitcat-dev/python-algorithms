# 1, 2, 3, 4, 8 / "6"
# 5, 4, 3, 2, -1

# 2, 3, 5, 9 / "10"
# 8, 7, 5, 1

# 배열을 가지고 해싱함수를 만든다?
# 두 합이 타겟
# 대칭 키를 싹저장하고, 2개 뽑을 수 있으면 true?


def solution(arr, target):
    dict = {}
    # 전체 탐색 해서 필요한 대칭 값 추출
    for i in arr:
        # 해싱 처리해서 딕셔너리로
        reverse = target - i
        # 필요없는 경우 제외 (동일하거나, 음수의 경우)
        if reverse == i or reverse < 0:
            continue
        else:
            dict[reverse] = i

        # print(dict)

    # 전체 탑색 해서 대칭값 리스트에 존재하는지 확인
    for i in arr:
        if i in dict:
            return True

    return False


res = solution([1, 2, 3, 4, 8], 6)
print(res)

res = solution([2, 3, 5, 9], 10)
print(res)

res = solution([2, 3, 5, 9, 7], 16)
print(res)

res = solution([], 16)
print(res)

# arr 에서 임의의 원소 x + k = target이 되는 원소 k가 존재하는지 확인

# 핵심은 k를 확인하는 동작의 효율 (전체검사를 돌리면 N제곱)

# 원소의 유무를 표시할 수 있는 해시 테이블 만들기

# 해시 테이블을 n개만큼 생성해서, 존재 여부를 T/F로 주입

# 두 수의 합이 해시 테이블에 인덱스로 검색해서 T면 True
