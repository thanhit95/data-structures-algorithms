from .testbase import print_tree
from binarytree import AvlTree


def do_task():
    avl = AvlTree(lst=[10, 20, 30, 40, 50, 25])

    print('\n size:', avl.size())
    print('\n min:', avl.min())
    print('\n max:', avl.max())
    print('\n contain:', avl.contain(50))
    print('\n height:', avl.height())

    print('\n print tree')
    print_tree(avl)

    print()
