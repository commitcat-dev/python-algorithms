# Union-Find (Disjoint Set Union, DSU) 서로소 집합 관리 자료구조

# 유즈케이스
### find(x): X가 속한 집합의 대표자(루트)를 찾는다.
### union(a, b): a가 속한 집합과 b가 속한 집합을 합친다.

### 위 두 연산을 이용해서, '사이클이 생기는지', '같은 집합에 속하는지'

# 샘플 코드


class UnionFind:
    # Parent[i]: i번의 부모 노드 (초기에는 자기 자신)

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # 부모가 내가 아닐 경우, 경로 압축
        if self.parent[x] != x:
            # 재귀로 동작하면서, 현재 노드(x)의 부모를 탐색, 동시에 부모 노드 역시 루트가아닐경우 재귀로 동작하면서 압축
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        # 각 원소의 루트 노드를 찾습니다. 만약 같다면 이미 합쳐진 친구이므로 정지
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False

        # 합치는 로직
        # Rank가 높다는 의미는 해당 트리가 더 깊다는 의미
        # 낮은 쪽을 높은 쪽의 자식으로 붙인다.
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            # 가장 처음 합쳐질 경우 높이 개념이 없으므로 일단 합치고 특정 노드의 랭크를 높인다.
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

    # 부모가 같은지 확인한다 == 같은 집합에 속했는지 확인한다.
    def connected(self, a, b):
        return self.find(a) == self.find(b)


# 5개의 요소(0,1,2,3,4)를 관리
uf = UnionFind(5)
print(uf.parent)
print(uf.rank)

# 처음엔 모두 다른 집합
print(uf.connected(0, 1))  # False

# 0과 1을 같은 집합으로 합치기
uf.union(0, 1)
print(uf.connected(0, 1))  # True

# 2와 3 합치기
uf.union(2, 3)

# 1과 2를 합치면, {0,1} 과 {2,3} 이 하나로 연결
uf.union(1, 2)
print(uf.connected(0, 3))  # True

# 이미 연결되어 있으면 False 반환
print(uf.union(0, 3))  # False

print(uf.parent)
print(uf.rank)
