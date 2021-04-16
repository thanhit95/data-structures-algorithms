#ifndef __TEST_DISPLAY_01_HPP__
#define __TEST_DISPLAY_01_HPP__


#include <iostream>
#include <string>
#include <vector>
#include "binarytree/binsearchtree.hpp"
#include "binarytreedisp/bintreedisplay.hpp"

using namespace my::test;
using namespace my::bt;
using namespace my::btdisp;



namespace my
{
namespace test
{
namespace display01
{



void doTask()
{
    auto bst = BinSearchTree<double>();

    std::vector<double> arrValue = {100, 50, 70000, 10, 88.523816, 20000, 90000, -123456, 14.78, 62, 500, 30000.19, 40000};

    for ( auto &&value : arrValue )
    {
        bst.insert(value);
    }

    auto disp = BinTreeDisplay();
    disp.config(
        '-',    // lineChar
        1,      // lineBrsp
        0,      // marginLeft
        2       // floatPre
    );

    auto res = bst.display(disp);

    std::cout << res << std::endl;
    std::cout << std::endl;
}



}
} // test
} // my



#endif
