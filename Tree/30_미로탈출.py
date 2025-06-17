# https://school.programmers.co.kr/learn/courses/30/lessons/159993

# 1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다. 각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동할 수 있습니다.
# 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다.
# 레버 또한 통로들 중 한 칸에 있습니다. 따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다.
# 이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다. 미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때, 최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.
# 미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요. 만약, 탈출할 수 없다면 -1을 return 해주세요.

# 제한사항
# 5 ≤ maps의 길이 ≤ 100
# 5 ≤ maps[i]의 길이 ≤ 100
# maps[i]는 다음 5개의 문자들로만 이루어져 있습니다.
# S : 시작 지점
# E : 출구
# L : 레버
# O : 통로
# X : 벽
# 시작 지점과 출구, 레버는 항상 다른 곳에 존재하며 한 개씩만 존재합니다.
# 출구는 레버가 당겨지지 않아도 지나갈 수 있으며, 모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있습니다.

from collections import deque

# 상, 하, 좌, 우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(maps):
    # 2중 배열
    col = len(maps[0])
    row = len(maps)
    array = [[0 for c in range(col)] for r in range(row)]

    start = (0, 0)
    lever = (0, 0)
    end = (0, 0)

    for i, map in enumerate(maps):
        for j, c in enumerate(map):
            array[i][j] = c
            if c == "S":
                start = (i, j)
            if c == "L":
                lever = (i, j)
            if c == "E":
                end = (i, j)
    # print(start, lever, end)

    # for i in array:
    #     for j in i:
    #         print(j, end=" ")
    #     print()

    #너비 우선 탐색을 하되, L을 먼저 찾고 L에서부터 제거해나가면서 E를 찾는다
    
    def bfs(start, target):
        visited = [[False for c in range(col)] for r in range(row)]
        q = deque()

        q.append((start[0], start[1], 0))
        visited[start[0]][start[1]] = True
        # print(visited)

        while q:
            x, y, d = q.popleft()
            # print(f"({x}, {y} 에서 거리 {d})")

            for dx, dy in direction:
                next_x = dx + x
                next_y = dy + y

                if 0 <= next_x < col and 0 <= next_y < row:
                    if not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        # print("#", array[next_x][next_y])

                        if array[next_x][next_y] == "X":
                            continue
                        elif array[next_x][next_y] == target:
                            return d + 1
                        else:
                            q.append((next_x, next_y, d + 1))


    first = bfs(start, "L")
    if not first:
        return -1
    second = bfs(lever, "E")
    if not second:
        return -1
    return first + second



maps1 = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
result1 = 16
maps2 = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]
result2 = -1

print(solution(maps=maps1))
print(solution(maps=maps2))
