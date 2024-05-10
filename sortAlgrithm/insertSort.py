'''插入排序 时间复杂度O(n^2) 适用于总体有序元素较少的情况'''


def insert(swaplist, index1, index2):
    tmpv = swaplist[index1]
    swaplist[index1] = swaplist[index2]
    swaplist[index2] = tmpv

def insertSort(lst: list):
    # tmp = lst.copy()
    for i in range(len(lst) - 1):
        for j in range(i + 1):
            if lst[j] < lst[i + 1]:
                continue
            else:
                insert(lst, j, i + 1)
    for j in range(len(lst) - 1):
        if lst[j] < lst[-1]:
            continue
        else:
            insert(lst, j, -1)

    return lst
'''1 8 5 9'''

