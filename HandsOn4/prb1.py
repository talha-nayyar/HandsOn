import heapq

def merge_sorted_arrays(arrays):
    min_heap = []
    result = []
    
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
    
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)
        
        if element_index + 1 < len(arrays[list_index]):
            next_tuple = (arrays[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return result

arrays = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
#arrays = [[1, 3, 7], [2, 4, 8], [9, 10, 11]]
print("Merged Sorted Arrays:", merge_sorted_arrays(arrays))

# 1  Time Complexity :  O(N*K log K) where N is the size of each array and K is number of arrays.
#                       This is because each insertion or extraction operation in a heap takes O(log K) time.

# 2  Improvement :      Could use a balanced BST instead of heap would optimize retrieval operations.