def merge_sort(arr):
    """
    Sorts an array using merge sort.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    """
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

test_array = [5, 2, 4, 7, 1, 3, 2, 6]
sorted_array = merge_sort(test_array)
print("Merge Sorted Array:", sorted_array)