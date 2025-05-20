input_1="baabaa"
input_2="cdcd"

# Stack 에 하나씩 저장.
# 마지막 요소를 비교했을 때, 동일하면 제거
def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            last_element = stack[-1]
            if last_element == c:
                stack.pop()
            else:
                stack.append(c)

    return len(stack) == 0


print(solution(input_1))
print(solution(input_2))
