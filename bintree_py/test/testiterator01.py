from .testbase import display_tree
from binarytree import BinSearchTree


def do_task():
    bst = BinSearchTree()

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.insert(value)

    print('\n display tree')
    display_tree(bst)

    print('\n\n using for each to iterate nodes in tree')

    for value in bst:
        print(value, end='  ')

    print('\n')
