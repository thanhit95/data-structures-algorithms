#ifndef __TEST_BST_01_HPP__
#define __TEST_BST_01_HPP__


#include <iostream>
#include <vector>
#include "binarytree/bst.hpp"


namespace mybt
{
namespace test
{



void printTree(BinarySearchTree<int> &bst)
{
    std::vector<int*> res = bst.traverse(TraverseOrder::IN);

    std::cout << "\n\n print tree: ";

    for (auto &&value : res)
    {
        std::cout << (*value) << "  ";
    }

    std::cout << std::endl;
}



void dotask()
{
    auto bst = BinarySearchTree<int>();

    for ( auto &&value : {12, 39, 20, 7, 26, 45, 19, 8} )
        bst.insert(value);

    // std::cout << bst;

    std::cout << "\n\n count: " << bst.count();

    std::cout << "\n\n min: " << *bst.getMin();

    std::cout << "\n\n max: " << *bst.getMax();

    std::cout << "\n\n get key: " << bst.get(20)->key;

    printTree(bst);


    /*
    std::cout << "\n\nUsing for each to iterate nodes in tree";

    for (auto &&value : bst)
        std::cout << value << std::endl;
    */


    bst.remove(800);
    bst.remove(12);

    std::cout << "\n\n count: " << bst.count();

    printTree(bst);


    std::cout << std::endl;
}



} // test
} // mybt


#endif
