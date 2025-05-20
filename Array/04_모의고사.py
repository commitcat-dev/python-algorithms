# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

answer_1 = [1, 2, 3, 4, 5]
return_1 = [1]
answer_2 = [1, 3, 2, 4, 2]
return_2 = [1, 2, 3]


# 1, 2, 3, 4, 5
def first_answer(number):
    if number % 5 == 0:
        return 5
    return number % 5


# 33, 11, 22, 44, 55
def third_answer(number):
    if number % 10 == 1:
        return 3
    if number % 10 == 2:
        return 3
    if number % 10 == 3:
        return 1
    if number % 10 == 4:
        return 1
    if number % 10 == 5:
        return 2
    if number % 10 == 6:
        return 2
    if number % 10 == 7:
        return 4
    if number % 10 == 8:
        return 4
    if number % 10 == 9:
        return 5
    if number % 10 == 0:
        return 5


# 2, 4, 6, 8
# 10, 12, 14, 16
# 18, 20, 22, 24
# 26, 28, 30, 32
# 1, 3, 4, 5
def second_answer(number):
    if number % 8 == 2:
        return 1
    if number % 8 == 4:
        return 3
    if number % 8 == 6:
        return 4
    if number % 8 == 0:
        return 5
    return 2


def my_solution(answers):
    answer = [0, 0, 0]
    answers_count = len(answers)
    for i in range(answers_count):
        current_answer = answers[i]
        answer_number = i + 1

        first_res = first_answer(answer_number)
        second_res = second_answer(answer_number)
        third_res = third_answer(answer_number)

        if first_res == current_answer:
            answer[0] += 1
        if second_res == current_answer:
            answer[1] += 1
        if third_res == current_answer:
            answer[2] += 1

    top_score = 0
    res = [1, 2, 3]

    for user in range(3):
        if answer[user] > top_score:
            top_score = answer[user]
            res = [user + 1]

        elif answer[user] == top_score:
            res.append(user + 1)

    return res


print(my_solution(answer_1))
print(my_solution(answer_2))
