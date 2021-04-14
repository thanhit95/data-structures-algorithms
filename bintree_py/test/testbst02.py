from .testbase import print_tree
from binarytree import BinSearchTree


def do_task():
    bst = BinSearchTree()

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.insert(value)

    print('\n print tree')
    print_tree(bst)

    print('\n height:', bst.height())

    print('\n')

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.remove(value)

    print('\n print tree')
    print_tree(bst)

    print('\n height:', bst.height())

    print()
