#include <iostream>
#include "binarytreetest/testtotal.hpp"


int main(int, char**)
{
    std::cout << "\n\n\n-----------------TEST BST 01" << std::endl;
    mybt::testbst01::dotask();

    std::cout << "\n\n\n-----------------TEST BST 02" << std::endl;
    mybt::testbst02::dotask();

    std::cout << "\n\n\n-----------------TEST AVL 01" << std::endl;
    mybt::testavl01::dotask();

    std::cout << "\n\n\n-----------------TEST AVL 02" << std::endl;
    mybt::testavl02::dotask();

    return 0;
}
