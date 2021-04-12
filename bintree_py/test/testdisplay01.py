from binarytree import BinSearchTree
from binarytreedisp import BinTreeDisplay


def dotask():
    # bst = BinarySearchTree(lst=[15, 20, 23, 25, 30, 35, 38, 40, 45])
    bst = BinSearchTree()

    # for value in [30, 9, 500, -5.1, 26, 144, 800, 12.85, -7, 288, 100.72]:
    #     bst.insert(value)

    for value in [100, 50, 70000, 10, 88.523816, 20000, 90000, -123456, 14.78, 62, 500, 30000.19, 40000]:
        bst.insert(value)

    print(bst)
    print()

    display = BinTreeDisplay()
    display.config(struct_node=('key', 'left', 'right'), line_brsp=1, margin_left=7, float_pre=3)

    res = display.get(bst._root)
    print(res)
