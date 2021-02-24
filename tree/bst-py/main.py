from libbst import BinarySearchTree


if __name__ == '__main__':
    bst = BinarySearchTree()

    for value in [12, 39, 20, 7, 26, 45, 8]:
        bst.insert(value)

    print(bst)

    bst.remove(12)

    print(bst)
