import Foundation

public final class TreeNode {
    var value: String
    var children: [TreeNode]

    public init(value: String) {
        self.value = value
        self.children = []
    }

    public func addChild(_ node: TreeNode) {
        children.append(node)
    }

    public func find(_ target: String) -> TreeNode? {
        if value == target {
            return self
        }
        for child in children {
            if let found = child.find(target) {
                return found
            }
        }
        return nil
    }
}

extension TreeNode {
    public func printTree(indent: String = "") {
        print(indent + value)
        for child in children {
            child.printTree(indent: indent + "  ")
        }
    }

    public func prettyPrint(level: Int = 0, prefix: String = "") {
        let indent = String(repeating: "    ", count: level)
        print("\(indent)\(prefix)\(value)")
        for (index, child) in children.enumerated() {
            let isLast = index == children.count - 1
            child.prettyPrint(level: level + 1, prefix: isLast ? "└── " : "├── ")
        }
    }

    public func printTreeHorizontally() {
        var queue: [(node: TreeNode, level: Int)] = [(self, 0)]
        var levels: [[String]] = []
        var maxLevel = 0

        while !queue.isEmpty {
            let (node, level) = queue.removeFirst()
            if level >= levels.count {
                levels.append([])
            }
            levels[level].append(node.value)
            for child in node.children {
                queue.append((child, level + 1))
            }
            maxLevel = max(maxLevel, level)
        }

        // 출력 (들여쓰기 간격 조절)
        let maxWidth = Int(pow(2.0, Double(maxLevel))) * 4
        for (i, level) in levels.enumerated() {
            let space = maxWidth / Int(pow(2.0, Double(i) + 1))
            let spacer = String(repeating: " ", count: space)
            let line = level.map { spacer + $0 + spacer }.joined()
            print(line)
        }
    }

    public func bfsTraverse() {
        var queue: [TreeNode] = [self]
        while !queue.isEmpty {
            let node = queue.removeFirst()
            print(node.value)
            queue.append(contentsOf: node.children)
        }
    }

    public func dfsTraverse() {
        print(value)
        for c in children {
            c.dfsTraverse()
        }
    }

    public func dfsStackVersion() {
        var stack: [TreeNode] = [self]

        while !stack.isEmpty {
            let node = stack.removeLast()
            print(node.value)
            for child in node.children.reversed() {
                stack.append(child)
            }
        }
    }

    // 재귀 DFS
    public func dfsRecursive() {
        print(value)
        for child in children {
            child.dfsRecursive()
        }
    }

    // 스택 DFS
    public func dfsStack() {
        var stack: [TreeNode] = [self]
        while !stack.isEmpty {
            let current = stack.removeLast()
            print(current.value)
            for child in current.children.reversed() {
                stack.append(child)
            }
        }
    }
}
