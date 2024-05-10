import time

def binary_search(lst: list, target: int, left: int, right: int) -> int:
    if left >= right:
        return None

    mid = left + (right - left) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, left, mid)
    else:
        return binary_search(lst, target, mid + 1, right)