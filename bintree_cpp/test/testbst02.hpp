#ifndef __TEST_BST_02_HPP__
#define __TEST_BST_02_HPP__


#include <iostream>
#include "testbase.hpp"
#include "binarytree/binsearchtree.hpp"

using namespace my::test;
using namespace my::bt;



namespace my
{
namespace test
{
namespace bst02
{



void doTask()
{
    auto bst = BinSearchTree<int>();

    for ( auto &&value : {12, 39, 20, 7, 26, 45, 19, 8} )
        bst.insert(value);

    base::printTree(bst);
    std::cout << " height: " << bst.height() << std::endl;


    for ( auto &&value : {12, 39, 20, 7, 26, 45, 19, 8} )
        bst.remove(value);

    base::printTree(bst);
    std::cout << " height: " << bst.height() << std::endl;


    std::cout << std::endl;
}



}
} // test
} // my



#endif
