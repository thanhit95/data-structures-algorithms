#ifndef __TEST_BASE_HPP__
#define __TEST_BASE_HPP__


#include <iostream>
#include <vector>
#include "binarytree/traversal/ordertraversal.hpp"
#include "binarytree/bintree.hpp"
#include "binarytreedisp/bintreedisplay.hpp"

using namespace my::bt;
using namespace my::btdisp;



namespace my
{
namespace test
{
namespace base
{



template <typename TKey, typename TNode>
void printTree(const BinTree<TKey, TNode> &tree, OrderTraversal order = OrderTraversal::IN)
{
    auto res = tree.traverse(order);

    for (auto &&value : res)
    {
        std::cout << value << "  ";
    }

    std::cout << std::endl;
}



template <typename TKey, typename TNode>
void displayTree(const BinTree<TKey, TNode> &tree)
{
    BinTreeDisplay disp;

    disp.config(
        '-',    // lineChar
        1,      // lineBrsp
        0,      // marginLeft
        2       // floatPre
    );

    auto res = tree.display(disp);
    std::cout << res << std::endl;
}



}
} // testbase
} // my



#endif // __TEST_BASE_HPP__
