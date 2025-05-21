input_1 = 10
input_2 = 27
input_3 = 12345


def solution(decimal):
    res = []
    remainder = decimal
    if remainder == 0:
        return "0"
    while remainder > 1:
        quotient = remainder % 2
        remainder = remainder // 2
        res.append(quotient)
    res.append(remainder)

    string = ""
    while res:
        string += str(res.pop())

    return string


print(solution(input_1))
print(solution(input_2))
print(solution(input_3))
