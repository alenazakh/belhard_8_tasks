"""
Реализовать алгоритм двоичного дерево поиска

Бинарное дерево поиска (BST) — это дерево, в котором все узлы следуют указанным
ниже свойствам. Левое поддерево узла имеет ключ, меньший или равный ключу его
родительского узла. Правое поддерево узла имеет ключ больше, чем ключ его
родительского узла. Таким образом, BST делит все свои поддеревья на два сегмента:
левое поддерево и правое поддерево и может быть определено как -
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)


https://tproger.ru/translations/binary-search-tree-for-beginners/
"""


class Tree_Node:
    level: int

    def __init__(self, data, level=0):
        self.left = None
        self.right = None
        self.data = data
        self.level = level

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree_Node(data)
                    self.level += 1
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree_Node(data)
                    self.level += 1
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root = Tree_Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
