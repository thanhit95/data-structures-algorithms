#ifndef __TEST_BST_02_HPP__
#define __TEST_BST_02_HPP__


#include <iostream>
#include <vector>
#include "binarytree/bst.hpp"

using namespace my::bt;



namespace my
{
namespace testbst02
{



void printTree(BinarySearchTree<int> &bst)
{
    std::vector<int*> res = bst.traverse(OrderTraverse::IN);

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

    printTree(bst);


    for ( auto &&value : {12, 39, 20, 7, 26, 45, 19, 8} )
        bst.remove(value);

    printTree(bst);

    std::cout << std::endl;
}



} // test
} // my



#endif
