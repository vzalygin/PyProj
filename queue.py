def empty(capacity=4): return [0, 0, [None] * capacity]
def size(queue): return (queue[1] - queue[0]) % len(queue[2])
def push(queue, x):
    capacity = len(queue[2])
    if size(queue) == capacity - 1:
        new_queue = empty(capacity * 2)
        for _ in range(capacity - 1): push(new_queue, pop(queue))
        queue[:] = new_queue
    queue[2][queue[1]] = x
    queue[1] += 1
    if queue[1] == len(queue[2]): queue[1] = 0
def pop(queue):
    result = queue[2][queue[0]]
    queue[0] += 1
    if queue[0] == len(queue[2]): queue[0] = 0
    return result


