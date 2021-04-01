#include <iostream>
#include "test/testtotal.hpp"


int main(int, char**)
{
    std::cout << "\n\n\n-----------------TEST BST 01" << std::endl;
    my::testbst01::dotask();

    std::cout << "\n\n\n-----------------TEST BST 02" << std::endl;
    my::testbst02::dotask();

    std::cout << "\n\n\n-----------------TEST AVL 01" << std::endl;
    my::testavl01::dotask();

    std::cout << "\n\n\n-----------------TEST AVL 02" << std::endl;
    my::testavl02::dotask();

    std::cout << "\n\n\n-----------------TEST DISPLAY 01" << std::endl;
    my::testdisplay01::dotask();

    return 0;
}
