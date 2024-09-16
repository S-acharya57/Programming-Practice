import visualize
import numpy as np 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr, i  # Yield the current state of the array and current index
        
        arr[j + 1] = key
        yield arr, i


visualize.sort(np.random.randint(1, 100, size=30), insertion_sort, speed=0.0001, gif_name="insertion_sort_30.gif")