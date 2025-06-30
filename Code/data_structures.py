from collections import deque
from heapq import heappush, heappop

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None

class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft() if self.items else None

class MinHeap:
    def __init__(self):
        self.heap = []
    def push(self, item):
        heappush(self.heap, item)
    def pop(self):
        return heappop(self.heap) if self.heap else None

# Example usage
stack = Stack()
stack.push("Book1")
stack.push("Book2")
print("Stack pop:", stack.pop())

queue = Queue()
queue.enqueue("Person1")
queue.enqueue("Person2")
print("Queue dequeue:", queue.dequeue())

heap = MinHeap()
heap.push(3)
heap.push(1)
print("Heap pop:", heap.pop())