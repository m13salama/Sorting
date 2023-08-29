import random

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

if __name__ == "__main__":
    arr = [54, 23, 1220, 9]
    sorted_arr = bogo_sort(arr)
    print(sorted_arr)
