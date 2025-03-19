import random

def quickselect(arr, low, high, i):
    if low == high:
        return arr[low]

    pivot_index = random_partition(arr, low, high)
    k = pivot_index - low + 1  # Position of pivot in sorted order

    if i == k:  # Found the ith order statistic
        return arr[pivot_index]
    elif i < k:
        return quickselect(arr, low, pivot_index - 1, i)
    else:
        return quickselect(arr, pivot_index + 1, high, i - k)

def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example Usage
arr = [12, 3, 5, 7, 19, 26]
i = 3  # Find the 3rd smallest element
print(f"The {i}th smallest element is: {quickselect(arr, 0, len(arr) - 1, i)}")

class Stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.top = -1
        self.size = size

    def push(self, x):
        if self.top == self.size - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.top == -1:
            raise Exception("Stack Underflow")
        x = self.stack[self.top]
        self.top -= 1
        return x

    def peek(self):
        if self.top == -1:
            raise Exception("Stack is Empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

# Example Usage
stack = Stack(5)
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20

class Queue:
    def __init__(self, size):
        self.queue = [0] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            raise Exception("Queue Overflow")
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = x

    def dequeue(self):
        if self.front == -1:
            raise Exception("Queue Underflow")
        x = self.queue[self.front]
        if self.front == self.rear:  # Queue is now empty
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return x

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

# Example Usage
queue = Queue(5)
queue.enqueue(5)
queue.enqueue(10)
print(queue.dequeue())  # Output: 5

class SinglyLinkedList:
    def __init__(self, size):
        self.data = [0] * size
        self.next = [-1] * size  # Stores index of the next node
        self.head = -1
        self.free = 0  # Points to the next free slot
        for i in range(size - 1):
            self.next[i] = i + 1  # Initialize free list
        self.next[size - 1] = -1  # Last element has no next

    def insert(self, x):
        if self.free == -1:
            raise Exception("List Overflow")
        new_node = self.free
        self.free = self.next[self.free]  # Update free slot
        self.data[new_node] = x
        self.next[new_node] = self.head  # Insert at head
        self.head = new_node

    def delete(self, x):
        prev = -1
        curr = self.head
        while curr != -1:
            if self.data[curr] == x:
                if prev == -1:
                    self.head = self.next[curr]
                else:
                    self.next[prev] = self.next[curr]
                self.next[curr] = self.free
                self.free = curr
                return
            prev = curr
            curr = self.next[curr]
        raise Exception("Element not found")

    def display(self):
        curr = self.head
        while curr != -1:
            print(self.data[curr], end=" -> ")
            curr = self.next[curr]
        print("None")

# Example Usage
ll = SinglyLinkedList(5)
ll.insert(10)
ll.insert(20)
ll.display()  # Output: 20 -> 10 -> None
ll.delete(10)
ll.display()  # Output: 20 -> None
