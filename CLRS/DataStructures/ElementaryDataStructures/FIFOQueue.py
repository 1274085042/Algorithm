
class Queue:
    def __init__(self, n: int):
        self.array = [None] * (n + 1)
        self.tail = 0
        self.head = 0  # index of head
        self.size = n  # index of next location where a new element will be inserted

    def is_empty(self):
        return self.head == self.tail
    
    def enqueue(self, x):
        """Add an element to the tail of the queue"""
        # Check for queue overflow. Must always have at least 1 empty slots
        if self.head == (self.tail + 1) % (self.size + 1):
            raise RuntimeError("Queue is full")
        else:
            self.array[self.tail] = x
            # Wrap around index of tail if the end of queue is reached
            self.tail = (self.tail + 1) % (self.size + 1)

    def dequeue(self):
        """Remove an element from the head of queue"""
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        else:
            out = self.array[self.head]
            self.head = (self.head + 1) % (self.size +1)
            return out

    def __str__(self):
        """Return the string representation of the queue, from head to tail"""
        if self.is_empty():
            return str([])
        else:
            if self.head < self.tail:
                return str(self.array[self.head : self.tail])
            else :
                return str(self.array[self.head:]+self.array[:self.tail])  


# Testing
if __name__ == "__main__":

    queue1 = Queue(11)
    # Put in 6 values.
    for i in range(100, 106):
        queue1.enqueue(i)
    print(queue1)  
    for i in range(6):
        print(queue1.dequeue())
    print(queue1.is_empty())
    queue1.enqueue(15)
    queue1.enqueue(6)
    queue1.enqueue(9)
    queue1.enqueue(8)
    queue1.enqueue(4)
    print(queue1)
    queue1.enqueue(17)
    print(queue1)
    queue1.enqueue(3)
    print(queue1)
    queue1.enqueue(5)
    print(queue1)
    print(queue1.dequeue())
    print(queue1)

    # Empty queue1 and then try to dequeue.
    while not queue1.is_empty():
        queue1.dequeue()
    try:
        queue1.dequeue()  # error when dequeueing from empty queue
    except RuntimeError as e:
        print(e)

    # Queue overflow.
    queue2 = Queue(10)
    for i in range(9):
        queue2.enqueue(i)
    print(queue2)
    try:
        queue2.enqueue(9)
        print(queue2)
        queue2.enqueue(10)
    except RuntimeError as e:
        print(e)
