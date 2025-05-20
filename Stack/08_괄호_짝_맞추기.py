# ( , ) s
input_1 = "(())()"
input_2 = "((())()"


def solution(s):
    open_bracket = []
    close_bracket = []

    for i in s:
        if i == "(":
            if len(close_bracket) == 0:
                print("못 만나서 추가")
                open_bracket.append(1)
            else:
                # close_bracket은 필요가 없는 프로퍼티
                print("열린괄호가 닫힌괄호를 만나버렸다")
                close_bracket.pop()
        else:
            if len(open_bracket) == 0:
                print("열린 괄호가 없는데 닫힌 괄호가 오면 짝이 안맞아요")
                return False
            else:
                print("닫힌괄호가 열린괄호를 만나버렸다")
                open_bracket.pop()

    if len(open_bracket) == 0 and len(close_bracket) == 0:
        return True
    else:
        return False


res = solution(input_1)
print(res)
res = solution(input_2)
print(res)

input_3 = ")((())()"
res = solution(input_3)
print(res)
