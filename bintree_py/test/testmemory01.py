from binarytree import AvlTree
from binarytreedisp import BinTreeDisplay


def dotask():
    display = BinTreeDisplay()

    a = AvlTree()

    for value in [10, 20, 30, 40, 50, 25]:
        a.insert(value)

    b = a.clone()
    print('\nDISPLAY b')
    print(display.get(b.root))

    c = a.clone()
    c.clear()
    print('\nDISPLAY c')
    print(display.get(c.root))
