from binarytree import AvlTree
from binarytreedisp import BinTreeDisplay


def dotask():
    display = BinTreeDisplay()

    avl = AvlTree(candd_removal='right')

    for value in [10, 20, 30, 40, 50, 25, 100, 28, 140]:
        avl.insert(value)

    print(display.get(avl.root), end='\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    for value in [30, 50, 140, 25, 20, 10, 40, 100, 28]:
        print(f'REMOVES {value} \n')
        avl.remove(value)
        print(display.get(avl.root), end='\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    # print(avl)
    # print()
