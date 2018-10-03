"""main function"""
import midHeap

if __name__ == '__main__':
    l0 = [0, 1, 2, 3, 4, 5, 6, 7]
    l1 = [1, 64, 78, 234, 6]

    print(midHeap.build_min_heap(l0))
    print(midHeap.build_min_heap(l1))