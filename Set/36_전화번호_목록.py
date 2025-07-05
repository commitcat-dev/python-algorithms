def solution(phone_book):
    answer = True
    return answer


# 효율성 실패, 테스트 케이스 실패
def solution2(phone_book):
    phone_length_list = []
    _set = set()

    # 1. 접두사로 검색할 수 있는 가짓수를 확인 O(N)
    # [2, 3, 7, 9]
    # 2. 전체 리스트를 Set에 저장 + 접두사 가능 만큼 스플릿
    # O(N^2)인데 그럼..

    for num in phone_book:
        phone_length_list.append(len(num))

    phone_length_list.sort()

    for num in phone_book:
        for length in phone_length_list:
            if len(num) <= length:
                break
            else:
                _set.add(num[:length])

    for num in phone_book:
        if num in _set:
            return False
        else:
            continue

    answer = True
    return answer


# phone_book	                    | return
# ----------------------------------------
# ["119", "97674223", "1195524421"]	| false
# ["123","456","789"]	            | true
# ["12","123","1235","567","88"]	| false

print(solution2(["119", "97674223", "1195524421"]))
print(solution2(["123", "456", "789"]))
print(solution2(["12", "123", "1235", "567", "88"]))
