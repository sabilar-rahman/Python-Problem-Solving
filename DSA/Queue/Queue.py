# Queue implementation in Python

# Creating a queue
def create_queue():
    queue = []
    return queue


# Checking if the queue is empty
def check_empty(queue):
    return len(queue) == 0


# Adding items into the queue (enqueue)
def enqueue(queue, item):
    queue.append(item)
    print("enqueued item: " + item)


# Removing an element from the queue (dequeue)
def dequeue(queue):
    if (check_empty(queue)):
        return "queue is empty"

    return queue.pop(0)  # Removes the first item inserted


# Using the queue
queue = create_queue()
enqueue(queue, str(1))
enqueue(queue, str(2))
enqueue(queue, str(3))
enqueue(queue, str(4))
print("dequeued item: " + dequeue(queue))
print("queue after dequeuing an element: " + str(queue))
