# Bartosz Wrobel, 302940
from typing import List
import unittest, random
from timeit import timeit

def partition(list: List[int], start: int, stop:int) -> int:
    i = start - 1
    pivot = list[stop]
    for j in range(start, stop):
        if list[j] <= pivot:
            i += 1
            container = list[i]
            list[i] = list[j]
            list[j] = container

    container = list[i+1]
    list[i+1] = list[stop]
    list[stop] = container

    return i + 1

def quicksort(list: List[int]) -> List[int]:
    list_tmp = list[:]
    def quicksort_core(list, start, stop):
        if start < stop:
            pi = partition(list, start, stop)

            quicksort_core(list, start, pi - 1)
            quicksort_core(list, pi + 1, stop)
            return list
    return quicksort_core(list_tmp, 0, len(list_tmp)-1)

def bubblesort(list: List[int]) -> (List[int], int):
    list_tmp = list[:]
    n = len(list_tmp)
    comparison_count = 0
    is_sorted = True
    while n>1 and is_sorted:
        is_sorted=False
        for i in range(1, n):
            comparison_count += 1
            is_sorted = True
            if list_tmp[i-1] > list_tmp[i]:
                container = list_tmp[i-1]
                list_tmp[i-1] = list_tmp[i]
                list_tmp[i] = container
                is_sorted = True
        n-=1
    return (list_tmp, comparison_count)

if __name__ == '__main__':
    unittest.main()
    #timeit tests random
    test_list = random.sample(range(1,1000), 600)
    t1_bubble = (timeit("bubblesort(test_list)", number=100, globals=globals()))
    t1_quicksort = (timeit("quicksort(test_list)", number=100, globals=globals()))
    print('timeit_random:')
    print(t1_bubble)
    print(t1_quicksort)

    #timeit tests sorted
    test_list_presorted = [1,2,3,4,5,6,7,8,9,10]
    t2_bubble = (timeit("bubblesort(test_list_presorted)", number=100, globals=globals()))
    t2_quicksort = (timeit("quicksort(test_list_presorted)", number=100, globals=globals()))
    print('timeit_sorted:')
    print(t2_bubble)
    print(t2_quicksort)

    #timeit tests reverse-sorted
    test_list_reverse = [10,9,8,7,6,5,4,3,2,1]
    t3_bubble = (timeit("bubblesort(test_list_reverse)", number=100, globals=globals()))
    t3_quicksort = (timeit("quicksort(test_list_reverse)", number=100, globals=globals()))
    print('timeit_reverse-sorted:')
    print(t3_bubble)
    print(t3_quicksort)

    #timeit tests equal values
    test_list_equal = [1,1,1,1,1,1,1,1,1]
    t4_bubble = (timeit("bubblesort(test_list_equal)", number=100, globals=globals()))
    t4_quicksort = (timeit("quicksort(test_list_equal)", number=100, globals=globals()))
    print('timeit_equal_values:')
    print(t4_bubble)
    print(t4_quicksort)
    # Wnioski z timeit:
    # Algorytm quicksort jest wyraznie szybszy od bubblesort, co dobrze pokazuje sortowanie dlugiej listy losowej.
    # 100-krotne posortowanie identycznej listy 600-elementowej zajelo bullesortowi 7.87 sekundy, zas quicksortowi 0.24.
    # Daje to srednie: 0.0787s bubblesort, 0.0024s quicksort.

# Bartosz Wrobel, 302940