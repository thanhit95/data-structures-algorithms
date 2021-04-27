#ifndef __TEST_BST_01_HPP__
#define __TEST_BST_01_HPP__


#include <iostream>
#include "testbase.hpp"
#include "binarytree/binsearchtree.hpp"

using namespace my::test;
using namespace my::bt;



namespace my
{
namespace test
{
namespace bst01
{



void doTask()
{
    auto bst = BinSearchTree<int>();

    for ( auto &&value : {12, 39, 20, 7, 26, 45, 19, 8} )
        bst.insert(value);

    std::cout << "\n size: " << bst.size() << std::endl;
    std::cout << "\n min: " << bst.min() << std::endl;
    std::cout << "\n max: " << bst.max() << std::endl;
    std::cout << "\n contain: " << bst.contain(20) << std::endl;
    std::cout << "\n height: " << bst.height() << std::endl;

    std::cout << "\n print tree:" << std::endl;
    base::printTree(bst);


    std::cout << "\n" << std::endl;


    bst.remove(800);
    bst.remove(12);

    std::cout << "\n size: " << bst.size() << std::endl;
    std::cout << "\n height: " << bst.height() << std::endl;

    std::cout << "\n print tree:" << std::endl;
    base::printTree(bst);


    std::cout << std::endl;
}



}
} // test
} // my



#endif
