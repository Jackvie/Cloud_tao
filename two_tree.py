class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.rchild = None
        self.lchild = None

class McTree(object):
    """完全二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root is None:
            self.root = Node(item)
            return
        queue = [self.root]
        while True:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = Node(item)
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = Node(item)
                return
            else:
                queue.append(cur_node.rchild)

    def travel(self):
        """广度遍历"""
        if self.root is None:
            return False
        queue = [self.root]
        while True:
            if not queue:
                return False
            cur_node = queue.pop(0)
            print(cur_node.item)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre(self):
        self.__preorder(self.root)

    def mid(self):
        self.__midorder(self.root)

    def after(self):
        self.__afterorder(self.root)

    def __preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.item)
        self.__preorder(node.lchild)
        self.__preorder(node.rchild)

    def __midorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.__midorder(node.lchild)
        print(node.item)
        self.__midorder(node.rchild)


    def __afterorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.__afterorder(node.lchild)
        self.__afterorder(node.rchild)
        print(node.item)


if __name__ == '__main__':
    t = McTree()
    for i in range(10):
        t.add(i)
    t.travel()
    print()
    t.pre()
    print()
    t.mid()
    print()
    t.after()








