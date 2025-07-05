def solution(n, costs):
    answer = 0
    # 가능한 조합을 전부다 계산?
    total_cost = 0
    for cost in costs:
        print(cost[0], cost[1], cost[2])
    return answer


# n	costs	                                    return
# 4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
# set?

solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])

# 0,1 | 0, 2 | 3, 4 이건 실패네 (전체 연결이 안되서)

# 노드 개념이 들어가야할 거 같고.
