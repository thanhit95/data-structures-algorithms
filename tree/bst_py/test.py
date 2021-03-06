from bst import BinarySearchTree


def test01():
    bst = BinarySearchTree(candd_removal='right')

    for value in [12, 39, 20, 7, 26, 45, 8]:
        bst.insert(value)

    print(bst)
    print('Count:', bst.count())

    rm_result = bst.remove(12)

    print(bst)
    print('Count:', bst.count())


#
#
def test02():
    # WARNING! THESE FOLLOWING 4 LINES OF CODE SHOULD BE MODIFIED TO INCLUDE MODULE "bintreedisplay" CORRECTLY.
    import sys
    sys.path.append('./tree/bintreedisp_py')
    sys.path.append('.')
    from tree.bintreedisp_py.bintreedisplay import BinTreeDisplay
    ###

    # bst = BinarySearchTree(lst=[15, 20, 23, 25, 30, 35, 38, 40, 45])
    bst = BinarySearchTree()

    # for value in [30, 9, 500, -5.1, 26, 144, 800, 12.85, -7, 288, 100.72]:
    #     bst.insert(value)

    for value in [100, 50, 70000, 10, 88, 20000, 900000, -123456, 14.78, 62, 500, 21000]:
        bst.insert(value)

    print(bst)
    print()

    display = BinTreeDisplay()
    # display.config(struct_node=('key', 'left', 'right'), dash_size=3, margin_left=7, float_format='{:.4f}')

    res = display.get(bst.root)
    print(res)


########################################################
########################################################


test02()
