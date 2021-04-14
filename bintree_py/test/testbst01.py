from .testbase import print_tree
from binarytree import BinSearchTree


def do_task():
    bst = BinSearchTree()

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.insert(value)

    print('\n count:', bst.count())
    print('\n min:', bst.min())
    print('\n max:', bst.max())
    print('\n contain:', bst.contain(20))
    print('\n height:', bst.height())

    print('\n print tree')
    print_tree(bst)

    print('\n')

    _ = bst.remove(800)
    _ = bst.remove(12)

    print('\n count:', bst.count())
    print('\n height:', bst.height())

    print('\n print tree')
    print_tree(bst)

    print()
