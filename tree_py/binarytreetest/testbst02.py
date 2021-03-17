from binarytree import BinarySearchTree
from binarytreedisp import BinTreeDisplay


def dotask():
    display = BinTreeDisplay()
    bst = BinarySearchTree(candd_removal='right')

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.insert(value)

    print(display.get(bst.root), end='\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    for value in [12, 39, 45, 20, 7, 26, 19, 8]:
        print(f'REMOVES {value} \n')
        bst.remove(value)
        print(display.get(bst.root), end='\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
