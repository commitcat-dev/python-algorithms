# ["i", "drink", "water"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"Yes"
# ["i", "water", "drink"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"No"


# 1 ~ 10
# 2 ~ n1 + n2
# n1 != n2

from collections import deque


def solution(cards1, cards2, goal):
    # 1. goal의 첫 번째를 가져온다.
    # 2. card1 과 card 2의 첫번째에 해당 값이 존재한다면 존재하는 값을 제거한다.
    # 2 - 1. 만약 존재하는 값이 없다면, False를 리턴
    # 3. goal에 값이 남아있는 값이 없으면 성공을 리턴하고, 아직 존재하면 1번으로 돌아간다.
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while len(goal) != 0:
        # 두 덱에 더 이상 뽑을 카드가 남지 않은 경우
        if not cards1 and not cards2:
            return "No"
        target = goal.popleft()
        print(goal)
        # 첫번째 덱과 일치하면 제거
        if cards1 and cards1[0] == target:
            cards1.popleft()
            continue

        # 두번째 덱과 일치하면 제거
        if cards2 and cards2[0] == target:
            cards2.popleft()
            continue
        # 두 덱에 목표가 없으므로 실패
        return "No"

    # Goal을 성공적으로 제거했으므로 성공
    return "Yes"


res = solution(
    ["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]
)
# res = solution(
#     ["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]
# )
print(res == "Yes")
