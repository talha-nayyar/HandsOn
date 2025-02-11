def remove_duplicates(arr):
    if not arr:
        return []
    
    unique_index = 0  #ptr for unique
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
    
    return arr[:unique_index + 1]

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print("Array after removing duplicates:", remove_duplicates(arr))

# 1  Time Complexity :  O(N) because the array is only traversed once.

# 2  Improvement :      Use of extra space, aka Hash set could reemove duplicates in O(N) while still maintaining order.