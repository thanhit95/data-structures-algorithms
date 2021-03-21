#include <iostream>
#include "binarytree/bst.hpp"

using namespace mybt;

int main(int, char**)
{
    std::cout << "Hello tree" << std::endl;

    BinarySearchTree<int> tree;

    tree.insert(50);
    tree.insert(25);
    tree.insert(80);
    tree.insert(10);
    tree.insert(40);
    tree.insert(90);

    auto res = tree.traverse(TraverseOrder::IN);

    for (auto &e : res)
    {
        std::cout << *e << std::endl;
    }

    BinNode<int> *getRes = tree.get(40);

    std::cout << "get res: " << getRes->key << std::endl;

    return 0;
}
