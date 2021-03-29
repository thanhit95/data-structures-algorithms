from binarytree import AvlTree
from binarytreedisp import BinTreeDisplay


def dotask():
    display = BinTreeDisplay()

    # avl = AvlTree(lst=[10, 20, 30, 40, 50])
    # avl.insert(25)

    avl = AvlTree()

    for value in [10, 20, 30, 40, 50, 25]:
        avl.insert(value)
        print(display.get(avl.root), end='\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

    # print(avl)
    # print()
