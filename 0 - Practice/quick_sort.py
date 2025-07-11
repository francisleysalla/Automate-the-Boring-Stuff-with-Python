# This is a quick sort algorithm without the use of comprehensions.

import logging
import random
logging.basicConfig(filename="0 - Practice/debug_quick_sort.txt", filemode="w", level = logging.DEBUG, format='%(levelname)s - %(message)s')

def quick_sort(arr, start = 0, end = None):
    if end is None:
        end = len(arr) - 1
    logging.disable(logging.NOTSET)
    logging.info(f"Starting quick sort on array: {arr[start:end]}")
    if (end - start) <= 0:
        return
    # Chose a pivot
    pivot = (end + start) // 2
    logging.info(f"Pivot chosen: {arr[pivot]} at index {pivot}")
    # Create a loop
    left_c = start
    right_c = end
    
    # Stop when both sides meet.
    while left_c < right_c:
        # Find an element to the left of the pivot that is greater than it.
        while arr[left_c] <= arr[pivot] and left_c < pivot:
            left_c += 1
        logging.debug(f"Left cursor at index {left_c} with value {arr[left_c]}" + 
                        ("\nThe left side reached the pivot.\n" if left_c == pivot else "\n"))

        # Find an element to the right of the pivot that is less than it.
        while arr[right_c] >= arr[pivot] and right_c > pivot:
            right_c -= 1
        logging.debug(f"Right cursor at index {right_c} with value {arr[right_c]}" +
                    ("\nThe right side reached the pivot.\n" if right_c == pivot else "\n"))

        # Swap them
        if left_c < right_c:
            arr[left_c], arr[right_c] = arr[right_c], arr[left_c]
            pivot = right_c if left_c == pivot else left_c if right_c == pivot else pivot
        logging.debug(f"Swap: {arr[left_c]} at index {left_c} with {arr[right_c]} at index {right_c}")
        logging.debug(f"Array after swap: {arr}")
        logging.debug(f"New pivot index: {pivot} - Value: {arr[pivot]}\n")
    
    
    logging.info(f"Array before recursion: {arr[start:end]}\n")
    assert all(arr[x] <= arr[pivot] for x in range(pivot)) and all(arr[x] >= arr[pivot] for x in range(pivot+1, len(arr)))
    quick_sort(arr, start, pivot-1)
    quick_sort(arr, pivot+1, end)
    return

        

data = [random.randint(0,999) for _ in range(40)]
print(f"Unsorted data: {data}")
quick_sort(data)
for i in range(len(data)-1):
    assert data[i] <= data[i+1], f"Array is not sorted at index {i}: {data[i]} > {data[i+1]}"
print(f"Sorted data:   {data}")