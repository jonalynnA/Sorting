# TO-DO: Complete the selection_sort() function below

""" def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
     """


import random
array = list(range(1, 21))
random.shuffle(array)


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):        # selection_sort takes in an array, i is the index starting at the 0 index and running through the length of the array -1 which would be the last indexed item
        cur_index = i                       # the current index we are on is represented with i
        smallest_index = cur_index          # Looking for the smallest index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # for each item (j) in the array with a range of index + 1 through length of the array
        for j in range(i + 1, len(arr)):
            # if the smallest index of the array is > array j:
            if arr[smallest_index] > arr[j]:
                smallest_index = j  # The smallest index of the array goes to j

# TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


array = list(range(1, 21))
random.shuffle(array)
print(array)
print(selection_sort(array))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):  # Outer loop: i = 0 to num of items in list minus 1
        # Inner loop: i = 0 to num of items in list minus 1 minus i because we know from the outer loop the last item in the list is already sorted
        for j in range(0, len(arr) - 1 - i):
            # if item on the left is bigger than item on the right:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap places
    return arr


array_2 = list(range(1, 21))
random.shuffle(array_2)
print(array_2)
print(bubble_sort(array_2))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
