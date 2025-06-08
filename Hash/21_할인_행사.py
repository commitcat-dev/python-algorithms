# XYZ
# XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여합니다.
# XYZ 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다.
# 할인하는 제품은 하루에 하나씩만 구매할 수 있습니다.
# 알뜰한 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.

# 예를 들어, 정현이가 원하는 제품이 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개이며,
# XYZ 마트에서 14일간 회원을 대상으로 할인하는 제품이 날짜 순서대로
# 치킨 , 사과,    사과, 바나나, 쌀,    사과, 돼지고기,
# 바나나, 돼지고기, 쌀,  냄비,   바나나, 사과, 바나나인 경우에 대해 알아봅시다.

# 첫째 날부터 열흘 간에는 냄비가 할인하지 않기 때문에 첫째 날에는 회원가입을 하지 않습니다.
# 둘째 날부터 열흘 간에는 바나나를 원하는 만큼 할인구매할 수 없기 때문에 둘째 날에도 회원가입을 하지 않습니다.
# 셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은 원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.
# 정현이가 원하는 제품을 나타내는 문자열 배열 want와 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number, XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때, 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오. 가능한 날이 없으면 0을 return 합니다.

# 제한사항
# 1 ≤ want의 길이 = number의 길이 ≤ 10
# 1 ≤ number의 원소 ≤ 10
# number[i]는 want[i]의 수량을 의미하며, number의 원소의 합은 10입니다.
# 10 ≤ discount의 길이 ≤ 100,000
# want와 discount의 원소들은 알파벳 소문자로 이루어진 문자열입니다.
# 1 ≤ want의 원소의 길이, discount의 원소의 길이 ≤ 12

# want	number	discount	result
w1 = ["banana", "apple", "rice", "pork", "pot"]
n1 = [3, 2, 2, 2, 1]
d1 = [
    "chicken",
    "apple",
    "apple",
    "banana",
    "rice",
    "apple",
    "pork",
    "banana",
    "pork",
    "rice",
    "pot",
    "banana",
    "apple",
    "banana",
]
r1 = 3

w2 = ["apple"]
n2 = [10]
d2 = [
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
]
r2 = 0


# O(n)
def solution(want, number, discount):
    dict = {}
    for i, w in enumerate(want):
        dict[w] = number[i]

    check = 0

    memo = {}

    # for i in range(10):
    #     key = discount[i]
    #     if key in memo:
    #         memo[key] += 1
    #     else:
    #         memo[key] = 1

    # memo가 요구사항과 동일하면 1 리턴
    # print(memo)
    # 아닐 경우 전체 탐색 시작
    # 1칸식 증가시키고 -10인덱스를 정상화

    for i, value in enumerate(discount):
        if i < 10:
            continue

        # 정답지에 해당 물건이 있고, 수량이 아직 넉넉하면 정답!
        if value in dict:
            check += 1
            dict[value] -= 1
            # 여기서 틀리면 10칸전 수정하고 한 칸 앞으로
            # print("In", value)
        else:
            check = 0
            memo = {}
            # 정답이 아니면 원상 복구할 필요가 없네 없으면 첨부터 다시

        # 정답이 10개 채워졌으면 해당 인덱스를 방출
        # if check == 10:
        #     return i

    # print(dict)
    return 0


print(solution(w1, n1, d1) == r1)
