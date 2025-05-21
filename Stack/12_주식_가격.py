# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# 초 단위로 기록된 주식 가격
# 가격이 떨어지지 않은 기간?의 총 시간

# price: 2~ 100,000개
# 각 1원 ~ 만원
# O(n)?

input_1 = [1, 2, 3, 2, 3]
output = [4, 3, 1, 1, 0]

input_2 = [2, 2, 3, 1, 3, 1]


def solution_non_stack(prices):
    res = []
    n = len(prices)

    for i in range(n):
        time = 0
        for j in range(i + 1, n):
            time += 1
            if prices[i] > prices[j]:
                break
        res.append(time)

    print(res)
    return res


# input_2 = [1, 6, 9, 5]

# 1, 5, 4, 5, 7, 4


# O(2N)
# "길이를 확정한 주식을 이후 계산에서 제외하기"
# 1. 주식이 떨어지는 시점을 찾고
# 2. 확정되지 않은 주식들을 검사해서 확정
# 3. 확정된 주식을 제거
def solution(prices):
    print("주어진 배열:", prices)
    print("------------------")
    n = len(prices)
    answer = [0] * n
    stack = []

    # "목표는 전체 인덱스를 한 번만 돌아서 각 인덱스의 상승 기간을 확정짓는 것"
    for i in range(n):
        # 비교군이 없으면 스택 인덱스를 추가
        if not stack:
            stack.append(i)
        else:
            # 하락장일 경우 기간은 1 고정
            if prices[stack[-1]] > prices[i]:
                answer[i - 1] = 1
                stack.pop()

                # TODO: 이 부분에서 남은 스택에서 하락장이 발생한 친구가 있다면 확정
                while stack and prices[stack[-1]] > prices[i]:
                    index = stack.pop()
                    answer[index] = i - index

            stack.append(i)

        print(f"[index: {i}, price: {prices[i]}] 스택 현황:{stack}")

    # TODO: 하락장을 겪지 않은 친구들은 마지막 인덱스와의 시간으로 확정
    while stack:
        index = stack.pop()
        answer[index] = n - index - 1

    print("------------------")
    print("결과:", answer)
    return answer


# solution(input_2)
solution(input_1)
# print(output == solution(input_1))
