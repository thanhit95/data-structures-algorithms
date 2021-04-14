from .testbase import print_tree
from binarytree import AvlTree


def do_task():
    avl = AvlTree()

    for value in [10, 20, 30, 40, 50, 25, 100, 28, 140]:
        print('\n\n\n insert', value)
        avl.insert(value)
        print(' height:', avl.height())
        print_tree(avl)

    for value in [30, 50, 140, 25, 20, 10, 40, 100, 28]:
        print('\n\n\n remove', value)
        avl.remove(value)
        print(' height:', avl.height())
        print_tree(avl)

    print()
