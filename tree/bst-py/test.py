from bst import BinarySearchTree
from bintreedisplay import BinTreeDisplay


def test01():
    bst = BinarySearchTree(candd_removal='right')

    for value in [12, 39, 20, 7, 26, 45, 8]:
        bst.insert(value)

    print(bst)

    bst.remove(12)

    print(bst)


#
#
def test02():
    # bst = BinarySearchTree(lst=[15, 20, 23, 25, 30, 35, 38, 40, 45])

    bst = BinarySearchTree()

    # for value in [30, 9, 500, -5.1, 26, 144, 800, 12.85, -7, 288, 100.72]:
    #     bst.insert(value)

    for value in [100, 50, 70000, 10, 88, 20000, 900000, -123456, 14.78, 62, 500, 21000]:
        bst.insert(value)

    print(bst)

    print()

    displayer = BinTreeDisplay()
    res = displayer.get_str(bst, dash_size=3)

    print(res)


########################################################
########################################################


test02()
