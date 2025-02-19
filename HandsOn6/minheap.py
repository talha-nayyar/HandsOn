class MinHeap:
    def __init__(self, data=None):
        """Initialize the heap with list of elements"""
        self.heap = data if data else []
        if self.heap:
            self.build_min_heap()

    def parent(self, i):
        """Returns the index of the parent node using bit manipulation"""
        return (i - 1) >> 1  # (i-1) // 2

    def left(self, i):
        """Returns the index of the left child node using bit manipulation"""
        return (i << 1) + 1  # 2*i + 1

    def right(self, i):
        """Returns the index of the right child node using bit manipulation"""
        return (i << 1) + 2  # 2*i + 2

    def swap(self, i, j):
        """Swaps two elements in the heap"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, i):
        """Ensures the min-heap property is maintained from index i downwards"""
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def build_min_heap(self):
        """Builds a min-heap from an unordered list"""
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)

    def insert(self, value):
        """Inserts a new value into the heap"""
        self.heap.append(value)
        i = len(self.heap) - 1

        # Bubble up the inserted element if necessary
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def pop(self):
        """Removes and returns the minimum element (root) from the heap"""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        root = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self.heapify(0)

        return root

    def peek(self):
        """Returns the minimum element without removing it"""
        if not self.heap:
            return None
        return self.heap[0]

    def __repr__(self):
        return f"MinHeap({self.heap})"
    
    
# Test heap functionality
heap = MinHeap([9, 5, 6, 2, 3])

print("Initial Min Heap:", heap)

heap.insert(1)
print("After inserting 1:", heap)

print("Minimum element (peek):", heap.peek())

print("Extract min:", heap.pop())
print("Heap after pop:", heap)

print("Extract min again:", heap.pop())
print("Heap after second pop:", heap)

heap.insert(4)
print("After inserting 4:", heap)

heap.insert(0)
print("After inserting 0:", heap)

print("Extract min (final test):", heap.pop())
print("Heap after final pop:", heap)
