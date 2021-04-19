import random


class arraySort:

    @property
    def array(self):
        array = list(range(300))
        random.shuffle(array)
        return array

    def Bubble(self):
        '''
        冒泡排序
        它重复地走访过要排序的数列，一次比较两个元素，
        如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
        也就是说该数列已经排序完成
        '''
        array = self.array
        length = len(array)
        for i in range(length):
            for j in range(length-i):
                if j==length-i-1:
                    continue
                if array[j]>array[j+1]:
                    temp = array[j+1]
                    array[j+1] = array[j]
                    array[j] = temp
        return array

    def Selection(self):
        '''
        选择排序
        首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
        然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        以此类推，直到所有元素均排序完毕
        '''
        array = self.array
        length = len(array)
        for i in range(length):
            min_index = i
            for j in range(i, length, 1):
                if array[j] < array[min_index]:
                    min_index = j
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
        return array

    def Insertion(self):
        '''
        插入排序
        它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
        '''
        array = self.array
        length = len(array)
        # 右测无序序列
        for i in range(1, length):
            # 左侧有序序列
            j = i - 1
            value = array[i]
            while j>=0:
                if value<array[j]:
                    array[j+1] = array[j]
                    array[j] = value
                    j -= 1
                else:
                    break
        return array

    def Shell(self):
        '''
        希尔排序是希尔（Donald Shell） 于1959年提出的一种排序算法。
        希尔排序也是一种插入排序，它是简单插入排序经过改进之后的一个更高效的版本，也称为缩小增量排序，
        同时该算法是冲破O(n2）的第一批算法之一。
        它与插入排序的不同之处在于，它会优先比较距离较远的元素。
        希尔排序又叫缩小增量排序。

        希尔排序是把记录按下表的一定增量分组，对每组使用直接插入排序算法排序；
        随着增量逐渐减少，每组包含的关键词越来越多，
        当增量减至1时，整个文件恰被分成一组，算法便终止。
        '''
        length = len(array)
        pass

    @staticmethod
    def _merge(left:list, right:list):
        new_array = list()
        l_len = len(left)
        r_len = len(right)
        l_cursor = r_cursor = 0
        while True:
            if l_cursor == l_len and r_cursor < r_len:
                new_array.extend(right[r_cursor:])
                break
            if r_cursor == r_len and l_cursor < l_len:
                new_array.extend(left[l_cursor:])
                break

            if left[l_cursor] <= right[r_cursor]:
                new_array.append(left[l_cursor])
                l_cursor += 1
            else:
                new_array.append(right[r_cursor])
                r_cursor += 1

        return new_array

    def MergeSort(self, array:list=None):
        '''
        归并排序，是创建在归并操作上的一种有效的排序算法。
        算法是采用分治法（Divide and Conquer）的一个非常典型的应用，且各层分治递归可以同时进行。
        归并排序思路简单，速度仅次于快速排序，为稳定排序算法，一般用于对总体无序，但是各子项相对有序的数列。
        归并排序是用分治思想，分治模式在每一层递归上有三个步骤：
        分解（Divide）：将n个元素分成个含n/2个元素的子序列。
        解决（Conquer）：用合并排序法对两个子序列递归的排序。
        合并（Combine）：合并两个已排序的子序列已得到排序结果。
        '''
        if array is None:
            array = self.array
        length:int = len(array)
        if length <2: return array
        left = array[0:length // 2].copy()
        right = array[length//2:].copy()
        return self._merge(self.MergeSort(left), self.MergeSort(right))

    def quicktion(self, array=None, low=None, high=None):
        '''
        快速排序使用分治法（Divide and conquer）策略
        选定基准值 把一个序列（list）分为较小和较大的2个子序列，
        然后递归地排序两个子序列。
        '''
        if array is None:
            array = self.array
            low = 0
            high = len(array)-1
            return self.quicktion(array, low=low, high=high)
        if low >= high:
            return
        # 基准值 选取第一个元素
        basevalue = array[low]
        i = low+1
        for j in range(low+1, high+1):
            if array[j] <= basevalue:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[low], array[i-1] = array[i-1], array[low]
        self.quicktion(array, low=low, high=i-2)
        self.quicktion(array, low=i, high=high)
        return array

    def HeapSort(self):
        pass

if __name__ == '__main__':
    p = arraySort()
    print(p.Bubble())
    print(p.Selection())
    print(p.Insertion())
    print(p.MergeSort())
    print(p.quicktion())
    print(p.HeapSort())