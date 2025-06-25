import math


def solution(n, words):
    _set = set()
    last_word = ""

    # 전체 탐색, 중복 및 규칙이 틀릴 경우
    for index, word in enumerate(words):
        if index == 0:
            _set.add(word)
        else:
            last_index = len(last_word)
            if last_word[last_index - 1] == word[0] and word not in _set:
                _set.add(word)
            else:
                # 틀린 경우 현재 인덱스 반환 그리고 누구인지
                current_user = index % n  # 현재 인덱스의 순ㅐ
                current_order = math.floor(index / n)
                return [current_user + 1, current_order + 1]

        last_word = word

    return [0, 0]


# n	| words	                                                                                    | result
# -----------------------------------------------------------------------------------------------------
# 3	| ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	            | [3,3]
# 5	| ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
#      "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	| [0,0]
# 2	| ["hello", "one", "even", "never", "now", "world", "draw"]	                                | [1,3]

print(
    solution(
        3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    )
)
