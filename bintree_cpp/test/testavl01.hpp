#ifndef __TEST_AVL_01_HPP__
#define __TEST_AVL_01_HPP__


#include <iostream>
#include "testbase.hpp"
#include "binarytree/avltree.hpp"

using namespace my::test;
using namespace my::bt;



namespace my
{
namespace test
{
namespace avl01
{



void doTask()
{
    auto avl = AvlTree<int>();

    for ( auto &&value : {10, 20, 30, 40, 50, 25} )
        avl.insert(value);

    std::cout << "\n count: " << avl.count() << std::endl;
    std::cout << "\n min: " << avl.min() << std::endl;
    std::cout << "\n max: " << avl.max() << std::endl;
    std::cout << "\n contain: " << avl.contain(50) << std::endl;
    std::cout << "\n height: " << avl.height() << std::endl;

    std::cout << "\n print tree:" << std::endl;
    base::printTree(avl);

    std::cout << std::endl;
}



}
} // test
} // my



#endif
