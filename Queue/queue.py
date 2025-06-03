from collections import deque
import time

lst = list(range(100000))
dq = deque(range(100000))

# pop

start_time = time.time()
for i in range(100000):
    lst.pop(0)

print("소요 시간: ", time.time() - start_time)


start_time = time.time()
for i in range(100000):
    dq.popleft()
print("소요 시간: ", time.time() - start_time)

deque_sample = deque([1, 2, 3])
print(deque_sample)
first = deque_sample.popleft()
print(deque_sample, first)

deque_sample2 = deque([1])
print(deque_sample2, deque_sample2.count)
# first = deque_sample2.popleft()
print(deque_sample2, first, deque_sample2.maxlen)
# first = deque_sample2.popleft()
# print(deque_sample2, first)

if deque_sample2:
    print("존재")
else:
    print("미존재")
