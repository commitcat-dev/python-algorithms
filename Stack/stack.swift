import Foundation

protocol Stack {
    associatedtype Item

    var isEmpty: Bool { get }
    var isFull: Bool { get }
    var top: Int { get }
    var data: [Item] { get }

    func push(item: Item)
    func pop() -> Item?
}

class StackImpl<Item>: Stack {
    var isEmpty: Bool {
        data.isEmpty
    }

    var isFull: Bool {
        data.count == maxSize
    }

    var top: Int = -1

    var data: [Item] = []

    private var maxSize: Int

    init(maxSize: Int) {
        self.maxSize = maxSize
    }

    func push(item: Item) {
        guard !isFull else { return }
        top += 1
        data.append(item)
    }

    @discardableResult
    func pop() -> Item? {
        guard !isEmpty else { return nil }
        top -= 1
        return data.removeLast()
    }
}

let stack = StackImpl<Int>(maxSize: 10)

stack.pop()
stack.push(item: 3)
print(stack.data)
stack.push(item: 5)
print(stack.data)
stack.pop()
print(stack.data)
stack.push(item: 6)
print(stack.data)

