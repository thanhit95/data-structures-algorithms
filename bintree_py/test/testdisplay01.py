from .testbase import print_tree
from binarytree import BinSearchTree
from binarytreedisp import BinTreeDisplay


def do_task():
    bst = BinSearchTree()

    for value in [100, 50, 70000, 10, 88.523816, 20000, 90000, -123456, 14.78, 62, 500, 30000.19, 40000]:
        bst.insert(value)

    disp = BinTreeDisplay()

    disp.config(struct_node=('key', 'left', 'right'), line_char='-', line_brsp=1, margin_left=0, float_pre=2)

    res = bst.display(disp)
    print(res)

    print()
