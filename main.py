import searchAlgrithm.BinarySearch as search
import time

if __name__ == '__main__':

    list1=[i for i in range(100**4)]
    binary_start = time.time()
    print(search.binary_search(list1, 10332000, 0, 100**4))
    print("binary used time: {}".format(time.time() - binary_start))

    # python_index_start = time.time()
    # list1.index(10000000)
    # print("python index used time: {}".format(time.time() - python_index_start))