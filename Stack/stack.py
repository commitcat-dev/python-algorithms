stack = []
max_size = 10


def isFull(stack):
    return len(stack) == max_size


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    if isFull(stack):
        print("스택이 가득 찼어요!")
    else:
        stack.append(item)
        print("데이터가 추가되었어요!", item)


def pop(stack):
    if isEmpty(stack):
        print("스택이 비었어요!")
        return None
    else:
        _item = stack.pop()
        print("데이터가 제거되었어요!", _item)
        return _item


push(stack=stack, item=3)
print(stack)
push(stack=stack, item=5)
print(stack)
pop(stack=stack)
print(stack)
push(stack=stack, item=6)
print(stack)
