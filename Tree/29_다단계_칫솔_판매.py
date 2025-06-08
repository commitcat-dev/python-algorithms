# https://school.programmers.co.kr/learn/courses/30/lessons/77486


class TreeNode:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self.income = 0

    def add_chile(self, node):
        self.children.append(node)

    def add_money(self, money):
        self.income += money


# (연습) 주어진 배열을 사용해서 트리 구조 만들기


def solution_시간초과(enroll, referral, seller, amount):
    answer = []
    center = TreeNode("center", "-")

    dict = {}

    # 사용자 트리로 변환하고 dict에서 관리
    for user in enroll:
        dict[user] = TreeNode(user, "-")

    # tree에 부모 설정
    for index, user in enumerate(enroll):
        tree = dict[user]

        if referral[index] == "-":
            tree.parent = center
        else:
            parent = referral[index]
            parent_tree = dict[parent]
            tree.parent = parent_tree

    for index, user in enumerate(seller):
        income = amount[index] * 100
        # print(user, income)
        user_tree = dict[user]
        node = user_tree
        while node != center:
            tax = income // 10
            _income = income - tax
            # print(tax, _income)
            node.add_money(_income)
            node = node.parent
            income = tax

    for user in enroll:
        node = dict[user]
        answer.append(node.income)

    # print(answer)
    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]

print(solution(enroll, referral, seller, amount))
