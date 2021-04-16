#ifndef __PARSING_NODE_HPP__
#define __PARSING_NODE_HPP__


#include <string>



namespace my
{
namespace btdisp
{



struct ParsingNode
{
    std::string key;
    ParsingNode *left = nullptr;
    ParsingNode *right = nullptr;

    int width = 0;
    int widthLeftBranch = 0;
    int widthRightBranch = 0;
    int sizeLeftLine = 0;
    int sizeRightLine = 0;

    int marginKey = 0;
    int marginLeftChild = 0;
    int marginRightChild = 0;



    ParsingNode(const std::string &key = ""): key(key)
    {

    }
};



} // btdisp
} // my



#endif // __PARSING_NODE_HPP__
