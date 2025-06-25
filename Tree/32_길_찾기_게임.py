# https://school.programmers.co.kr/learn/courses/30/lessons/42892?language=python3

from collections import deque


# 이진 트리 노드
class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.left = None
        self.right = None


# 시간 초과 및 런타임 에러
def solution(nodeinfo):
    node_list = []

    for index, (x, y) in enumerate(nodeinfo):
        node_list.append(Node(x=x, y=y, value=index + 1))

    # Y축 기준으로 순서 정렬, 동일할 경우 X축 기준ㅍ로 왼쪽 우선
    def sorting(node):
        return (-node.y, node.x)

    node_list.sort(key=sorting)

    # 노드 순서 확인
    # for node in node_list:
    #     print(node.x, node.y, node.value)

    # 트리 만들기
    def insert(parent, child):
        if child.x < parent.x:
            if parent.left is None:
                parent.left = child
            else:
                insert(parent.left, child)
        else:
            if parent.right is None:
                parent.right = child
            else:
                insert(parent.right, child)

    root = node_list[0]
    for node in node_list[1:]:
        insert(root, node)

    # 노드 출력
    def print_tree(node):
        q = deque()
        q.append(node)

        while q:
            node = q.popleft()
            print(f"Node { node.value } level {node.y}")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    # print_tree(root)

    # 전위 순회 (Preorder Traversal)
    def preorder(node, result):
        if node is None:
            return
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)

    pre = []
    preorder(root, pre)

    # 후위 순회 (Postorder Traversal)
    def postorder(node, result):
        if node is None:
            return
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)

    post = []
    postorder(root, post)

    return [pre, post]


# 좌표 기반 이진 트리
node = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
result = [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]

print(solution(node) == result)
