input_1 = "[](){}"
input_2 = "}]()[{"
input_3 = "[)(]"
input_4 = "}}}"


def solution(s):
    result = 0
    stack = list(s)
    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid_string(rotated):
            result += 1
    return result


def is_valid_string(s):
    stack = []
    for c in s:
        if c == "[" or c == "(" or c == "{":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                open_bracket = stack.pop()
                if c == "]" and open_bracket != "[":
                    return False
                elif c == ")" and open_bracket != "(":
                    return False
                elif c == "}" and open_bracket != "{":
                    return False

    return len(stack) == 0


print(solution(input_1))
print(solution(input_2))
print(solution(input_3))
print(solution(input_4))
