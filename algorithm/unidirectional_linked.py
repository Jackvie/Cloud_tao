
class Node(object):
    """节点"""
    def __init__(self, item):
        self.head = item
        self.next = None

class Signal(object):
    """单向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判空"""
        return self.__head == None

    def length(self):
        """长度"""
        curs = self.__head
        count = 0
        if self.is_empty():
            return count
        while True:
            count += 1
            if curs.next is None:
                return count
            curs = curs.next

    def append(self, item):
        """后入"""
        if self.is_empty():
            self.__head = Node(item)
            return
        curs = self.__head
        while True:
            if curs.next is None:
                curs.next = Node(item)
                break
            curs = curs.next

    def add_head(self, item):
        """头入"""
        node = Node(item)
        node.next, self.__head = self.__head, node

    def travel(self):
        """遍历"""
        if self.is_empty():
            return None
        curs = self.__head
        while True:
            print(curs.head, end=" ")
            curs = curs.next
            if curs is None:
                print()
                break

    def insert(self, index, item):
        """指入"""
        pre = self.__head
        if index == 0:
            self.add_head(item)
        elif index == self.length() - 1:
            self.append(item)
        else:
            count = 0
            while True:
                if count == index - 1:
                    node = Node(item)
                    node.next = pre.next
                    pre.next = node
                    return
                pre = pre.next
                count += 1

    def search(self, item):
        """搜寻"""
        curs = self.__head
        if self.is_empty():
            return False
        while True:
            if curs.head == item:
                return True
            curs = curs.next
            if curs is None:
                return False

    def delete(self, item):
        if self.is_empty():
            return False
        curs = self.__head
        pre = None
        while True:
            if curs.head == item:
                if self.__head == curs:
                    self.__head = curs.next
                    break
                pre.next = curs.next
                break
            if curs.next == None:
                return False
            pre = curs
            curs = curs.next


if __name__ == '__main__':
    l = Signal()
    l.add_head(11)
    l.append(1)
    l.append(2)
    l.append(3)
    l.add_head(10)

    l.travel()
    print(l.length())

    l.insert(0, 1000)
    l.travel()

    print(l.search(1000))

    l.travel()
    l.delete(11)
    l.travel()
