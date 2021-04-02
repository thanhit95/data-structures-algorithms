#ifndef __TEST_DISPLAY_01_HPP__
#define __TEST_DISPLAY_01_HPP__


#include <iostream>
#include <string>
#include <vector>
#include "binarytree/bst.hpp"
#include "binarytreedisp/display.hpp"

using namespace my::bt;
using namespace my::btdisp;



namespace my
{
namespace testdisplay01
{



void dotask()
{
    auto bst = BinarySearchTree<double>();

    std::vector<double> arrInsert = {100, 50, 70000, 10, 88.523816, 20000, 90000, -123456, 14.78, 62, 500, 30000.19, 40000};

    for ( auto &&value : arrInsert )
    {
        bst.insert(value);
    }

    auto display = BinTreeDisplay<BinNode<double>>();

    display.config('-', 1, 0, 2);

    auto res = display.get(bst._getRoot());

    std::cout << res;

    std::cout << std::endl;
}



} // test
} // my



#endif
