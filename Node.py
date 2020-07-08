class Node():
    __slots__ = 'root', 'leftchild', 'rightchild'
    def __init__(self, root, leftchild=None, rightchild=None):
        self.root = root
        self.leftchild = leftchild
        self.rightchild = rightchild