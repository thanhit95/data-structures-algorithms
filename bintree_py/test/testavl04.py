from .testbase import display_tree
from binarytree import AvlTree


def do_task():
    avl = AvlTree(canddrm='right')

    for value in [10, 20, 30, 40, 50, 25, 100, 28, 140]:
        print(f'\n\n\n\n insert {value} \n')
        avl.insert(value)
        display_tree(avl)

    print()

    for value in [30, 50, 140, 25, 20, 10, 40, 100, 28]:
        print(f'\n\n\n\n remove {value} \n')
        avl.remove(value)
        display_tree(avl)

    print()
