
class SortList(list):

    def bubble_sort(self):
        for i in range(len(self)-1,-1,-1):
            for j in range(0, i):
                if self[j] > self[j+1]:
                    temp = self[j+1]
                    self[j+1] = self[j]
                    self[j] = temp
                    
    def selection_sort(self):
            for j in range(len(self)):
                highest = [self[j],j]
                for i in range(j,len(self)):
                    if  highest[0] > self[i]:
                        highest[0] = self[i]
                        highest[1] = i
                self[j], self[highest[1]] = self[highest[1]], self[j]

    def insertion_sort(self):
            for i in range(1,len(self)):
                insert_position = i
                compare_value = self[i]
                for j in range(i-1,-1,-1):
                    if self[j] > compare_value:
                        self[j +1] = self[j]
                        insert_position = j
                    else:
                        break
                self[insert_position] = compare_value



    def quick_sort(self, start=0,end=None):
        if end is not None and start >= end:
            return
        if end is None:
            end = len(self)-1
        compare_value = self[start]
        first_index = start
        trade_first = False
        second_index = end
        trade_second = False
        while first_index < second_index:
            if self[first_index] < compare_value:
                first_index += 1
            else:
                trade_first = True
            if self[second_index] >= compare_value:
                second_index -= 1
            else:
                trade_second = True
            if trade_first and trade_second:
                self[first_index], self[second_index] = self[second_index],self[first_index]
                trade_first = False
                trade_second = False
        if self[first_index] <= compare_value:
            self.quick_sort(start,first_index)
            self.quick_sort(first_index+1,end)
        else:
            self.quick_sort(start,first_index-1)
            self.quick_sort(first_index,end)
