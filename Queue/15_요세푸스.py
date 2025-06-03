from collections import deque

# N = 1 ~ 1000
# K번째
# 1000이하


def solution(n, k):
    # [1 ~ N]
    dp = deque(range(1, n + 1))

    while len(dp) != 1:
        # 삭제 해야하는 인덱스 찾기
        target_index = k

        # k값 조절
        while target_index > len(dp):
            target_index -= len(dp)

        # 타겟 인덱스 기준으로 재정렬
        for i in range(1, target_index):
            data = dp.popleft()
            dp.append(data)

        # 타겟 인덱스 제거
        dp.popleft()

    return dp[0]


print(solution(2, 3) == 2)
print(solution(5, 2) == 3)
print(solution(5, 3) == 4)
