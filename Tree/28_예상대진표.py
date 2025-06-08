# N : 2^1 이상 2^20 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)
# A, B : N 이하인 자연수 (단, A ≠ B 입니다.)

import math


def solution(n, a, b):
    answer = 1

    if 근접한_상태_확인(a, b):
        return answer

    print(a, b, answer)

    # n을 나눠지지 않을 때까지 나눈다
    while n != 1:
        answer += 1
        n = n / 2
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        print(a, b, answer)
        if 근접한_상태_확인(a, b):
            return answer

    return answer


def 근접한_상태_확인(a, b):
    return min(a, b) % 2 == 1 and abs(b - a) == 1


def 틀렸던_풀이(a, b):
    return b % 2 == 0 and abs(b - a) == 1


# print(solution(8, 4, 7) == 3)
# print(solution(16, 1, 16) == 4)
# print(solution(8, 2, 3) == 2)
print(solution(64, 12, 53) == 5)

# 1, 2, 3, 4, 5, 6, 7, 8
#   1     2    3     4
#      1         2
#          1
