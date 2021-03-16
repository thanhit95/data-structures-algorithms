from bintree.bst import BinarySearchTree


def dotask():
    bst = BinarySearchTree(candd_removal='right')

    for value in [12, 39, 20, 7, 26, 45, 8]:
        bst.insert(value)

    print(bst)
    print('count:', bst.count())

    _ = bst.remove(12)

    print(bst)
    print('count:', bst.count())
