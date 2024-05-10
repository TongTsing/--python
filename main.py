import searchAlgrithm.BinarySearch as search
import sortAlgrithm.insertSort as st
import time

if __name__ == '__main__':
    print(st.insertSort([1,8,5,9]))
    # list1=[i for i in range(100**4)]
    # print("sleep 100s")
    # time.sleep(10)
    # print("start")
    # binary_start = time.time()
    # print(search.binary_search(list1, 10332000, 0, 100**4))
    # print("binary used time: {}".format(time.time() - binary_start))

    # python_index_start = time.time()
    # list1.index(10000000)
    # print("python index used time: {}".format(time.time() - python_index_start))