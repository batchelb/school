#!/usr/bin/env python3
from sort_list import SortList
import time
import copy

class Result:
    def __init__(self):
        self.name = None
        self.time = None
        self.relative = None
        self.first = None
        self.last = None

def create_1000_in_list_5_copy(array):
    l = []
    for i in range(1000):
        l.append(array)
        return [copy.deepcopy(l),copy.deepcopy(l),copy.deepcopy(l),copy.deepcopy(l),copy.deepcopy(l)]

def main():
    FILENAMES = [
        [ 'list1.txt', 'int'   ],
        [ 'list2.txt', 'int'   ],
        [ 'list3.txt', 'int'   ],
        [ 'list4.txt', 'int'   ],
        [ 'list5.txt', 'float' ],
        [ 'list6.txt', 'int'   ],
    ]
    full_lists_of_lists = []
    for files in FILENAMES:
        with open(files[0]) as f:
                full_lists_of_lists.append(create_1000_in_list_5_copy(SortList(map(eval(files[1]), f.read().splitlines()))))

    for index,test in enumerate(full_lists_of_lists):
        print('list'+str(index + 1)+'.text')
        results = []
        for i,copy_1000 in enumerate(test):
            result = Result()
            method = ['sort','insertion_sort','selection_sort','bubble_sort','quick_sort'][i]
            if i == 0:
                result.name = 'Native Language Sort'
            elif i == 1:
                result.name = 'Insertion Sort'
            elif i == 2:
                result.name ='Selection Sort'
            elif i == 3:
                result.name = 'Bubble Sort'
            else:
                result.name = 'Quicksort'
            start_time = time.clock() * 100
            for individual_list in copy_1000:
                getattr(individual_list,method)()
            end_time = time.clock()*100
            result.time = round(end_time-start_time,6)
            result.first = ', '.join(map(str,copy_1000[0][:10]))
            if len(copy_1000[0]) > 10:
                result.last = ', '.join(map(str,copy_1000[0][-10:len(copy_1000[0]):1]))
            else:
                result.last = ', '.join(map(str,copy_1000[0]))
            results.append(result)
        results.sort(key = lambda x: x.time)
        fastest_time = results[0].time
        for result in results:
            print(result.name)
            print(result.time)
            print(str(round(100.0 * (result.time - fastest_time) / fastest_time)) + '%')
            print('First 10: ', result.first)
            print('Last 10: ', result.last)
            print()


### Main runner ###
if __name__ == '__main__':
    main()
